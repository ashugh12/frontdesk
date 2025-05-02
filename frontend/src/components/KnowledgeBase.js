import React, { useState, useEffect } from "react";
import axios from "axios";

const KnowledgeBase = () => {
    const [knowledge, setKnowledge] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:5000/get_knowledge_base")
            .then(response => setKnowledge(response.data))
            .catch(error => console.error("Error fetching knowledge base:", error));
    }, []);

    return (
        <div>
            <h2>Knowledge Base</h2>
            <ul>
                {knowledge.map(entry => (
                    <li key={entry.query}>{entry.query}: {entry.answer}</li>
                ))}
            </ul>
        </div>
    );
};

export default KnowledgeBase;
