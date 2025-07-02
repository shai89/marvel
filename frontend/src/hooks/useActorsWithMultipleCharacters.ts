import { useEffect, useState } from "react";
import { getActorsWithMultipleCharacters } from "../api/movies";
import { ActorsWithMultipleCharacters } from "../types/models";

export const useActorsWithMultipleCharacters = () => {
  const [data, setData] = useState<ActorsWithMultipleCharacters>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getActorsWithMultipleCharacters()
      .then(setData)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { data, loading, error };
};
