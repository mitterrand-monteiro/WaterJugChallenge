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
    queue = [(0, 0)]
    actions = []

    while queue:
        current = queue.pop(0)
        if current[0] == z or current[1] == z:
            actions.append(current)
            return actions

        visited.add(current)
        a, b = current

        # Actions: Fill A, Fill B, Empty A, Empty B, Pour A to B, Pour B to A
        next_states = [
            (x, b),  # Fill A
            (a, y),  # Fill B
            (0, b),  # Empty A
            (a, 0),  # Empty B
            (min(x, a + b), max(0, a + b - x)),  # Pour A to B
            (max(0, a + b - y), min(y, a + b))   # Pour B to A
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                actions.append((a, b, state))
    return None  # No solution possible

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

@app.get("/water_jug_solution/", response_model=WaterJugResponse, tags=["Water Jug"])
async def get_water_jug_solution(x: int, y: int, z: int):
    solution = water_jug_solution(x, y, z)
    if solution:
        return {"solution": solution}
    else:
        return {"message": "No solution possible"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
