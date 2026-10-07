from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated Drone Swarm & Fusion State
zones_data = {
    "A2": {"sound": 40, "thermal": False, "vibration": False, "confidence": 42, "priority": "P3"},
    "C1": {"sound": 65, "thermal": True,  "vibration": False, "confidence": 68, "priority": "P2"},
    "B4": {"sound": 86, "thermal": True,  "vibration": True,  "confidence": 92, "priority": "P1"}
}

@app.websocket("/ws/simulation")
async def websocket_simulation(websocket: WebSocket):
    await websocket.accept()
    try:
        # Step 1: D1 Scanning Audio
        await websocket.send_json({"type": "STATUS", "drone": "D1", "zone": "B4", "msg": "Acoustic signal detected in Zone B4"})
        await asyncio.sleep(2)

        # Step 2: D2 Scanning Thermal
        await websocket.send_json({"type": "STATUS", "drone": "D2", "zone": "B4", "msg": "Thermal anomaly verified in Zone B4"})
        await asyncio.sleep(2)

        # Step 3: D3 Scanning Vibration
        await websocket.send_json({"type": "STATUS", "drone": "D3", "zone": "B4", "msg": "Vibration pulse detected under debris (depth up to 20ft)"})
        await asyncio.sleep(2)

        # Step 4: Sensor Fusion Calculation
        await websocket.send_json({
            "type": "FUSION_RESULT",
            "zone": "B4",
            "data": zones_data["B4"],
            "alert": "🚨 P1 - HIGH PRIORITY RESCUE REQUIRED AT ZONE B4"
        })
    except Exception as e:
        print(f"WebSocket closed: {e}")
        from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"zone": "B4", "sound": "YES", "thermal": "YES", "vibration": "YES", "confidence": 92, "priority": "P1"})