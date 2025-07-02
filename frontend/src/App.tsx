import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import MoviesPerActor from "./pages/MoviesPerActor";
import ActorsWithMultipleCharacters from "./pages/ActorsWithMultipleCharacters";
import CharactersWithMultipleActors from "./pages/CharactersWithMultipleActors";

function App() {
  return (
    <BrowserRouter>
      <nav className="bg-gray-100 p-4 flex gap-6">
        <Link className="text-blue-600 font-medium" to="/">Movies Per Actor</Link>
        <Link className="text-blue-600 font-medium" to="/actors">Actors w/ Multiple Characters</Link>
        <Link className="text-blue-600 font-medium" to="/characters">Characters w/ Multiple Actors</Link>
      </nav>
      <Routes>
        <Route path="/" element={<MoviesPerActor />} />
        <Route path="/actors" element={<ActorsWithMultipleCharacters />} />
        <Route path="/characters" element={<CharactersWithMultipleActors />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
