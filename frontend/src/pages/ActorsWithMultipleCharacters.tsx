import { useActorsWithMultipleCharacters } from "../hooks/useActorsWithMultipleCharacters";
import ActorRoleCard from "../components/ActorRoleCard";

export default function ActorsWithMultipleCharacters() {
  const { data, loading, error } = useActorsWithMultipleCharacters();

  if (loading) {
    return <div className="p-6 text-blue-500 font-medium text-center">Loading...</div>;
  }

  if (error || !data) {
    return <div className="p-6 text-red-500 font-medium text-center">Error: {error}</div>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">🎭 Actors With Multiple Characters</h1>
      <div className="space-y-6">
        {Object.entries(data).map(([actor, roles]) => (
          <ActorRoleCard key={actor} actorName={actor} roles={roles} />
        ))}
      </div>
    </div>
  );
}
