from fastapi import FastAPI
from typing import Tuple, List, Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class WaterJugRequest(BaseModel):
    x: int
    y: int
    z: int

class WaterJugResponse(BaseModel):
    solution: Optional[List[Tuple[int, int]]]
    message: Optional[str]

def water_jug_solution(x: int, y: int, z: int) -> Optional[List[Tuple[int, int]]]:
    """
    Solve the Water Jug problem using breadth-first search.
    """
    if z > max(x, y) or z % gcd(x, y) != 0:
        return None  # No solution possible

    visited = set()
    queue = [((0, 0), [])]  # Each queue element is a tuple of (current state, history)
    actions = []

    while queue:
        current, history = queue.pop(0)
        a, b = current
        if a == z or b == z:
            actions = [(0, 0)] + history + [current]
            return actions

        visited.add(current)

        # Actions: Fill A, Fill B, Empty A, Empty B, Pour A to B, Pour B to A
        next_states = [
            ((x, b), history + [current]),  # Fill A
            ((a, y), history + [current]),  # Fill B
            ((0, b), history + [current]),  # Empty A
            ((a, 0), history + [current]),  # Empty B
            ((min(x, a + b), max(0, a + b - x)), history + [current]),  # Pour A to B
            ((max(0, a + b - y), min(y, a + b)), history + [current])   # Pour B to A
        ]

        for state, hist in next_states:
            if state not in visited:
                queue.append((state, hist))

    return None  # No solution possible

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

@app.get("/water_jug_solution/", response_model=WaterJugResponse, tags=["Water Jug"])
async def get_water_jug_solution(x: int, y: int, z: int):
    solution = water_jug_solution(x, y, z)
    if solution:
        return {"solution": solution, "message": ""}
    else:
        return {"solution": [], "message": "No solution possible"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
