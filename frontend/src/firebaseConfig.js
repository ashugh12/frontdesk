// Import Firebase
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyDRXwryJJMBleudt7lS_6_K30qd_bd5VDU",
    authDomain: "frontdesk-3d251.firebaseapp.com",
    projectId: "frontdesk-3d251",
    storageBucket: "frontdesk-3d251.firebasestorage.app",
    messagingSenderId: "858289909829",
    appId: "1:858289909829:web:26d0aa820aa2bdfc2ef32c",
    measurementId: "G-R89WT4KMWZ"
  };

  
// Initialize Firebase & Firestore
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };
