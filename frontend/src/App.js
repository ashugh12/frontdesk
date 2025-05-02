import React from "react";
import HelpRequests from "./components/HelpRequests";
import SupervisorDashboard from "./components/SupervisorDashboard";
import KnowledgeBase from "./components/KnowledgeBase";

function App() {
    return (
        <div>
            <h1>Human-in-the-loop AI System</h1>
            <HelpRequests />
            <SupervisorDashboard />
            <KnowledgeBase />
        </div>
    );
}

export default App;
