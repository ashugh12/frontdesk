import React, { useState, useEffect } from "react";
import { collection, onSnapshot } from "firebase/firestore";  // Remove `getFirestore`
import { db } from "../firebaseConfig";  // Ensure correct path

const HelpRequests = () => {
    const [requests, setRequests] = useState([]);

    useEffect(() => {
        const unsubscribe = onSnapshot(collection(db, "help_requests"), (snapshot) => {
            const helpRequests = snapshot.docs.map(doc => ({
                id: doc.id,
                ...doc.data()
            }));
            setRequests(helpRequests);
            console.log("🔥 Real-time update:", helpRequests);
        });

        return () => unsubscribe();  // Cleanup listener on unmount
    }, []);

    return (
        <div>
            <h2>Pending Help Requests</h2>
            <ul>
                {requests.map(req => (
                    <li key={req.id}>{req.customer_query}</li>
                ))}
            </ul>
        </div>
    );
};

export default HelpRequests;
