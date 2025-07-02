export interface CharacterAppearance {
  movieName: string;
  characterName: string;
}

export interface ActorAppearance {
  movieName: string;
  actorName: string;
}

export interface Movie {
  id: number;
  movieTitle: string;
  tmdb_id: number;
}

export interface MoviePerActor {
  id: number;
  actorName: string;
  movies: Movie[];
}

export interface ApiResponse {
  items: MoviePerActor[];
  total: number;
  page: number;
  limit: number;
}


export type ActorsWithMultipleCharacters = Record<string, CharacterAppearance[]>;
export type CharactersWithMultipleActors = Record<string, ActorAppearance[]>;
