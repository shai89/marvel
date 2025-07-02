// import { useEffect, useState } from "react";
// import { getMoviesPerActor } from "../api/movies";
// import { MoviePerActor } from "../types/models";

// export const useMoviesPerActor = () => {
//   const [data, setData] = useState<MoviePerActor[]>([]);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState<string | null>(null);

//   useEffect(() => {
//     getMoviesPerActor()
//       .then(setData)
//       .catch((err) => setError(err.message))
//       .finally(() => setLoading(false));
//   }, []);

//   return { data, loading, error };
// };

import { useQuery } from "@tanstack/react-query";
import { fetchMoviesPerActor } from "../api/movies";
import { ApiResponse } from "../types/models";

export const useMoviesPerActor = (page: number) =>
  useQuery<ApiResponse, Error>({
    queryKey: ["moviesPerActor", page],
    queryFn: () => fetchMoviesPerActor(page),
    // keepPreviousData: true,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });