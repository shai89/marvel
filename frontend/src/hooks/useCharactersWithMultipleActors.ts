import { useEffect, useState } from "react";
import { getCharactersWithMultipleActors } from "../api/movies";
import { CharactersWithMultipleActors } from "../types/models";

export const useCharactersWithMultipleActors = () => {
  const [data, setData] = useState<CharactersWithMultipleActors>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getCharactersWithMultipleActors()
      .then(setData)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { data, loading, error };
};
