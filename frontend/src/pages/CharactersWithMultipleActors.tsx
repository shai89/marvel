import { useCharactersWithMultipleActors } from "../hooks/useCharactersWithMultipleActors";
import CharacterAppearance from "../components/CharacterAppearance";
import { CharactersWithMultipleActorsResponse } from "../types/characterTypes";

export default function CharactersWithMultipleActors() {
  const { data, loading, error } = useCharactersWithMultipleActors();

  if (loading) {
    return <div className="p-6 text-blue-500 text-center text-lg font-semibold">Loading...</div>;
  }

  if (error || !data) {
    return <div className="p-6 text-red-600 text-center font-medium">Error: {error}</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
        <span role="img" aria-label="actors">🧑‍🎭</span> Characters With Multiple Actors
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {Object.entries(data as CharactersWithMultipleActorsResponse).map(([character, appearances]) => (
          <div
            key={character}
            className="bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition-all p-5"
          >
            <h2 className="text-lg font-bold text-indigo-700 mb-3 flex items-center gap-2">
              {character}
            </h2>
            <ul className="space-y-2">
              {appearances.map((entry, idx) => (
                <CharacterAppearance
                  key={`${character}-${entry.actorName}-${idx}`}
                  actorName={entry.actorName}
                  movieName={entry.movieName}
                />
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
