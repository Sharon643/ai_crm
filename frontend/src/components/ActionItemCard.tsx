import { useMemo, useState } from "react";

import { updateActionItem } from "../services/actionItemApi";

import type { HCPActionGroup, Task } from "../types/actionItem";

import "./ActionItemCard.css";

interface Props {
  group: HCPActionGroup;
}

export default function ActionItemCard({ group }: Props) {
  const [expanded, setExpanded] = useState(true);

  const [tasks, setTasks] = useState(group.tasks);

  const pending = useMemo(
    () => tasks.filter((t) => t.status === "Pending"),
    [tasks]
  );

  const completed = useMemo(
    () => tasks.filter((t) => t.status === "Completed"),
    [tasks]
  );

  const progress =
    tasks.length === 0
      ? 0
      : Math.round((completed.length / tasks.length) * 100);

  async function toggle(task: Task) {
    const newStatus =
      task.status === "Pending"
        ? "Completed"
        : "Pending";

    try {
      await updateActionItem(task.id, newStatus);

      setTasks((prev) =>
        prev.map((t) =>
          t.id === task.id
            ? { ...t, status: newStatus }
            : t
        )
      );
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="hcp-card">

      <div
        className="hcp-header"
        onClick={() =>
          setExpanded(!expanded)
        }
      >
        <div>

          <h3>{group.hcp.name}</h3>

          <p>{group.hcp.hospital}</p>

        </div>

        <div className="header-right">

          <div className="progress-text">

            {completed.length}/{tasks.length} Complete

          </div>

        <div
        className={`expand ${expanded ? "open" : ""}`}
        >
        ▶
        </div>

        </div>

      </div>

      <div className="progress-bar">

        <div
          className="progress-fill"
          style={{
            width: `${progress}%`,
          }}
        />

      </div>

      {!expanded && null}

      {expanded && (
        <>

          {pending.length > 0 && (

            <>
              <h4>Pending</h4>

              {pending.map((task) => (
                <Row
                  key={task.id}
                  task={task}
                  toggle={toggle}
                />
              ))}

            </>
          )}

          {completed.length > 0 && (

            <>
              <h4 className="completed-title">

                Completed

              </h4>

              {completed.map((task) => (
                <Row
                  key={task.id}
                  task={task}
                  toggle={toggle}
                />
              ))}

            </>
          )}

        </>
      )}

    </div>
  );
}

interface RowProps {
  task: Task;

  toggle: (
    task: Task
  ) => void;
}

function Row({
  task,
  toggle,
}: RowProps) {

  return (
    <div className="task-row">

      <label>

        <input
          type="checkbox"
          checked={
            task.status === "Completed"
          }
          onChange={() =>
            toggle(task)
          }
        />

        <span>{task.title}</span>

      </label>

      <Priority priority={task.priority} />

    </div>
  );
}

function Priority({
  priority,
}: {
  priority: string;
}) {

  return (
    <span
      className={`priority ${priority.toLowerCase()}`}
    >
      {priority}
    </span>
  );
}