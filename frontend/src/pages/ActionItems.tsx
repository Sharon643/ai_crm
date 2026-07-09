import { useEffect, useState } from "react";

import Header from "../components/Header";
import ActionItemCard from "../components/ActionItemCard";

import { getActionItems } from "../services/actionItemApi";

import type { HCPActionGroup } from "../types/actionItem";

import "./ActionItems.css";

export default function ActionItems() {
  const [groups, setGroups] = useState<HCPActionGroup[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    document.title = "Action Items";
    loadActionItems();
  }, []);

  async function loadActionItems() {
    try {
      setLoading(true);

      const response = await getActionItems();

      setGroups(response.data);
    } catch (err) {
      console.error(err);
      setError("Failed to load action items.");
    } finally {
      setLoading(false);
    }
  }

  const filteredGroups = groups.filter((group) => {
    const searchTerm = search.toLowerCase();

    return (
      group.hcp.name.toLowerCase().includes(searchTerm) ||
      (group.hcp.hospital ?? "")
        .toLowerCase()
        .includes(searchTerm)
    );
  });

  return (
    <>
      <Header />

      <main className="action-items-page">
        <div className="action-items-header">
          <h2>AI Generated Action Items</h2>

          <p>
            These follow-up tasks were automatically generated from your
            Healthcare Professional interactions and organized by priority.
          </p>
        </div>

        <input
          className="search-box"
          placeholder="Search by Healthcare Professional or Hospital..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        {loading && (
          <div className="empty-state">
            <p>Loading action items...</p>
          </div>
        )}

        {!loading && error && (
          <div className="empty-state">
            <p>{error}</p>
          </div>
        )}

        {!loading && !error && filteredGroups.length === 0 && (
          <div className="empty-state">
            <h3>🎉 You're all caught up!</h3>

            <p>
              No pending action items were found. New follow-up tasks will
              automatically appear here whenever you save Healthcare Professional
              interactions.
            </p>
          </div>
        )}

        {!loading &&
          !error &&
          filteredGroups.map((group) => (
            <ActionItemCard
              key={group.hcp.id}
              group={group}
            />
          ))}
      </main>
    </>
  );
}