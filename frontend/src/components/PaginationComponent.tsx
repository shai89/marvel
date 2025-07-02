import React from "react";

type Props = {
  currentPage: number;
  total: number;
  limit: number;
  onPageChange: (page: number) => void;
};

const PaginationComponent = React.memo(({ currentPage, total, limit, onPageChange }: Props) => {
  const totalPages = Math.ceil(total / limit);

  return (
    <div className="flex items-center justify-center space-x-4 my-4">
      <button
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
        className="px-4 py-2 bg-gray-200 text-gray-500 rounded disabled:opacity-50"
      >
        ⬅️ Previous
      </button>
      <span>Page {currentPage}</span>
      <button
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage >= totalPages}
        className="px-4 py-2 border border-black rounded"
      >
        Next ➡️
      </button>
    </div>
  );
});

export default PaginationComponent;
