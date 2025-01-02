import React, { useEffect } from "react";
import { useParams } from "react-router-dom";

function Redirect() {
  const { shortCode } = useParams();

  useEffect(() => {
    const fetchOriginalUrl = async () => {
      try {
        const response = await fetch(`http://localhost:8000/shorten/${shortCode}`);
        if (!response.ok) {
          throw new Error("Failed to fetch original URL");
        }

        const data = await response.json();
        window.location.href = data.url;
      } catch (err) {
        console.error(err.message);
      }
    };

    fetchOriginalUrl();
  }, [shortCode]);

  return <p>Redirecting...</p>;
}

export default Redirect;