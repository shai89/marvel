import { useState, useCallback } from "react";
import { useMoviesPerActor } from "../hooks/useMoviesPerActor";
import PaginationComponent from "../components/PaginationComponent";
import ActorCard from "../components/ActorCard";
import { MoviePerActor } from "../types/models";

const MoviesPerActor = () => {
  const [page, setPage] = useState(1);
  const { data, isLoading, isError } = useMoviesPerActor(page);

  const handlePageChange = useCallback((newPage: number) => {
    setPage(newPage);
    window.scrollTo({ top: 0, behavior: "smooth" }); // UX טוב
  }, []);

  if (isLoading) return <div className="p-6 text-center text-blue-500 text-xl font-semibold">Loading...</div>;
  if (isError || !data) return <div className="p-6 text-center text-red-600">Error loading data.</div>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6 text-gray-800">🎬 Movies Per Actor</h1>

      <PaginationComponent
        currentPage={page}
        total={data.total}
        limit={data.limit}
        onPageChange={handlePageChange}
      />

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-6 my-6">
        {data.items.map((actor: MoviePerActor, index: number) => (
          <ActorCard key={`${actor.actorName}-${index}`} actor={actor} index={index} />
        ))}
      </div>

      <PaginationComponent
        currentPage={page}
        total={data.total}
        limit={data.limit}
        onPageChange={handlePageChange}
      />
    </div>
  );
};

export default MoviesPerActor;
