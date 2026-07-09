import type {
  ChangeEvent,
  FormEvent,
} from "react";

import "./InteractionForm.css";

import {
  useAppDispatch,
  useAppSelector,
} from "../redux/hooks";

import {
  resetForm,
  updateField,
} from "../redux/slices/interactionSlice";

import type {
  FormField,
} from "../redux/slices/interactionSlice";
import { createInteraction } from "../services/api";
import { addMessage, clearChat } from "../redux/slices/chatSlice";
import toast from "react-hot-toast";

export default function InteractionForm() {
  const dispatch = useAppDispatch();

  const form = useAppSelector(
    (state) => state.interaction
  );

  const handleChange = (
    e: ChangeEvent<
      HTMLInputElement |
      HTMLSelectElement |
      HTMLTextAreaElement
    >
  ) => {
    dispatch(
      updateField({
        field: e.target.name as FormField,
        value: e.target.value,
      })
    );
  };

const handleSubmit = async (
  e: FormEvent<HTMLFormElement>
) => {
  e.preventDefault();

  try {
    await createInteraction({
      hcpName: form.hcpName,
      hospital: form.hospital,
      interactionType: form.interactionType,
      date: form.date,
      time: form.time,
      attendees: form.attendees,
      topics: form.topics,
      materials: form.materials,
      sentiment: form.sentiment,
      outcome: form.outcome,
      followUp: form.followUp,
      summary: "",
    });

    toast.success("Interaction saved successfully.");

    dispatch(resetForm());

    dispatch(
      addMessage({
        sender: "assistant",
        message:
          "✅ Interaction saved successfully.\n\nYour action items have been generated. You can now ask me to:\n\n• Show my action items\n• Plan my visits for today\n• Prepare me for my meeting",
      })
    );

    setTimeout(() => {
      dispatch(clearChat());
    }, 3000);
  } catch (error) {
    console.error(error);

    toast.error(
      "Failed to save interaction. Please try again."
    );
  }
};

  return (
    <form
      className="interaction-form"
      onSubmit={handleSubmit}
    >
      <h2>Log HCP Interaction</h2>

      <div className="form-group">
        <label>HCP Name</label>

        <input
          name="hcpName"
          value={form.hcpName}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label>Interaction Type</label>

          <select
            name="interactionType"
            value={form.interactionType}
            onChange={handleChange}
          >
            <option value="">Select</option>
            <option value="In-Person Visit">In-Person Visit</option>
            <option value="Phone Call">Phone Call</option>
            <option value="Video Call">Video Call</option>
            <option value="Email">Email</option>
          </select>
      </div>

      <div className="row">
        <div className="form-group">
          <label>Date</label>

          <input
            type="date"
            name="date"
            value={form.date}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Time</label>

          <input
            type="time"
            name="time"
            value={form.time}
            onChange={handleChange}
          />
        </div>
      </div>

      <div className="form-group">
        <label>Attendees</label>

        <input
          name="attendees"
          value={form.attendees}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label>Topics Discussed</label>

        <textarea
          rows={3}
          name="topics"
          value={form.topics}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label>Materials Shared</label>

        <textarea
          rows={2}
          name="materials"
          value={form.materials}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label>Observed HCP Sentiment</label>

          <select
            name="sentiment"
            value={form.sentiment}
            onChange={handleChange}
          >
            <option value="">Select</option>
            <option value="Positive">Positive</option>
            <option value="Neutral">Neutral</option>
            <option value="Negative">Negative</option>
          </select>
      </div>

      <div className="form-group">
        <label>Outcome</label>

        <textarea
          rows={2}
          name="outcome"
          value={form.outcome}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label>Follow-up Actions</label>

        <textarea
          rows={2}
          name="followUp"
          value={form.followUp}
          onChange={handleChange}
        />
      </div>

      <button
        className="save-btn"
        type="submit"
        disabled={form.loading}
      >
        {
          form.loading
          ? "Saving..."
          : "Save Interaction"
        }
      </button>
    </form>
  );
}