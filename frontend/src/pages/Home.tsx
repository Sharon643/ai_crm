import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
import ChatPanel from "../components/ChatPanel";

import "./Home.css";

export default function Home() {
  return (
    <>
      <Header />

      <main className="home-container">
        <section className="left-panel">
          <InteractionForm />
        </section>

        <section className="right-panel">
          <ChatPanel />
        </section>
      </main>
    </>
  );
}