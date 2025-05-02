import React, { useState } from "react";
import axios from "axios";

const SupervisorDashboard = () => {
    const [response, setResponse] = useState("");
    const [requestId, setRequestId] = useState("");

    const submitResponse = () => {
        axios.post("http://localhost:5000/resolve_request", {
            request_id: requestId,
            response: response
        })
        .then(res => alert("Response submitted!"))
        .catch(err => console.error("Error submitting response:", err));
    };

    return (
        <div>
            <h2>Supervisor Panel</h2>
            <input type="text" placeholder="Request ID" onChange={e => setRequestId(e.target.value)} />
            <textarea placeholder="Your Response" onChange={e => setResponse(e.target.value)} />
            <button onClick={submitResponse}>Submit Response</button>
        </div>
    );
};

export default SupervisorDashboard;
