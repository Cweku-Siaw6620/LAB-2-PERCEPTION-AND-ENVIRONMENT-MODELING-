import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from datetime import datetime

from environment import DisasterEnvironment


class SensorAgent(Agent):
    class SenseBehaviour(CyclicBehaviour):
        async def run(self):
            # Simulate environment change
            self.agent.environment.update_environment()

            # Perceive environment
            percept = self.agent.environment.get_state()

            # Create log entry
            log_entry = (
                f"[{percept['timestamp']}] "
                f"Damage Severity Detected: {percept['damage_severity']}"
            )

            # Print event log
            print(log_entry)

            # Save event log to file
            with open("events.log", "a") as log_file:
                log_file.write(log_entry + "\n")

            # Sense every 3 seconds
            await asyncio.sleep(3)

    async def setup(self):
        print("SensorAgent started – monitoring disaster environment")
        self.environment = DisasterEnvironment()
        self.add_behaviour(self.SenseBehaviour())


async def main():
    agent = SensorAgent("my_agent@xmpp.jp", "qwerty111")
    await agent.start()

    # Run agent for observation period
    await asyncio.sleep(20)
    await agent.stop()
    print("SensorAgent stopped")


if __name__ == "__main__":
    import spade
    spade.run(main())
