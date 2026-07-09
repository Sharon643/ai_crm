import {
  useEffect,
  useRef,
  useState,
  type FormEvent,
} from "react";

import "./ChatPanel.css";

import { useAppDispatch, useAppSelector } from "../redux/hooks";

import {
  addMessage,
  setLoading,
  setError,
} from "../redux/slices/chatSlice";

import {
  setForm,
  updateSingleField,
} from "../redux/slices/interactionSlice";

import { sendChatMessage } from "../services/api";

type ToolResponse = {
  type: string;
  success: boolean;
  message: string;
  payload?: any;
};

export default function ChatPanel() {
  const dispatch = useAppDispatch();

  const { messages, loading } = useAppSelector(
    (state) => state.chat
  );

  const [input, setInput] = useState("");

  const messagesEndRef =
    useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const handleSubmit = async (
    e: FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    if (!input.trim() || loading) return;

    dispatch(
      addMessage({
        sender: "user",
        message: input,
      })
    );

    dispatch(setLoading(true));

    try {
      const response =
        await sendChatMessage(input);

      const tool: ToolResponse =
        response.data;

      dispatch(
        addMessage({
          sender: "assistant",
          message: tool.message,
        })
      );

      switch (tool.type) {
        case "log":
          if (tool.payload) {
            dispatch(
              setForm(tool.payload)
            );
          }
          break;

        case "edit":
          if (tool.payload) {
            dispatch(
              updateSingleField({
                field: tool.payload.field,
                value: tool.payload.value,
              })
            );
          }
          break;

        case "meeting":
          // Will be implemented later
          break;

        case "planner":
          // Will be implemented later
          break;

        case "actions":
          // Will be implemented later
          break;

        default:
          console.warn(
            "Unknown tool:",
            tool.type
          );
      }
    } catch (error) {
      console.error(error);

      dispatch(
        setError("Failed to contact AI.")
      );

      dispatch(
        addMessage({
          sender: "assistant",
          message:
            "Sorry, I couldn't process your request.",
        })
      );
    } finally {
      dispatch(setLoading(false));
      setInput("");
    }
  };

  return (
    <div className="chat-container">
      <h2>AI Assistant</h2>

      <div className="messages">
        {messages.length === 0 && (
          <div className="empty-chat">
            <p>
              Describe your interaction with a
              Healthcare Professional.
            </p>

            <p>
              The AI will extract the details,
              populate the interaction form,
              and assist you throughout the
              workflow.
            </p>
          </div>
        )}

        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender}`}
          >
            {message.message}
          </div>
        ))}

        {loading && (
          <div className="message assistant typing">
            Thinking...
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form
        className="chat-input"
        onSubmit={handleSubmit}
      >
        <input
          type="text"
          placeholder="Describe an interaction or ask the AI to edit the extracted form..."
          value={input}
          onChange={(e) =>
            setInput(e.target.value)
          }
          disabled={loading}
        />

        <button
          type="submit"
          disabled={loading}
        >
          {loading
            ? "Thinking..."
            : "Send"}
        </button>
      </form>
    </div>
  );
}