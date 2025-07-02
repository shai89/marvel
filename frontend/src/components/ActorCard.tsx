import { MoviePerActor } from "../types/models";

type Props = {
  actor: MoviePerActor;
  index: number;
};

const ActorCard = ({ actor, index }: Props) => {
  return (
    <div
      key={`${actor.actorName}-${index}`}
      className="bg-white border border-gray-200 rounded-lg shadow p-4 hover:shadow-lg transition"
    >
      <h2 className="text-blue-700 font-semibold text-lg mb-2">{actor.actorName}</h2>
      <ul className="list-inside text-sm text-gray-800 space-y-1">
        {actor.movies.map((movie, i) => (
          <li key={`${movie.movieTitle}-${i}`}>
            <span className="font-medium">{movie.movieTitle}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActorCard;
