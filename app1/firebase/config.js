import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCKefrnaxgfQUTZuas-YU_1nG7xJhPeMEE",
  authDomain: "healthapp-c1ca3.firebaseapp.com",
  projectId: "healthapp-c1ca3",
  storageBucket: "healthapp-c1ca3.appspot.com",
  messagingSenderId: "414902720016",
  appId: "1:414902720016:web:4aa63d086f76d3c9451c95",
  measurementId: "G-E41LK49Y70"
};

// Initialize Firebase
const firebase_app = initializeApp(firebaseConfig);
export default firebase_app;