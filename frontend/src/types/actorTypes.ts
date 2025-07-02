export interface Movie {
  id: number;
  movieTitle: string;
  tmdb_id: number;
}

export interface ActorData {
  id: number;
  actorName: string;
  movies: Movie[];
}

export interface ApiResponse {
  items: ActorData[];
  total: number;
  page: number;
  limit: number;
}

export interface ActorRole {
  characterName: string;
  movieName: string;
}
