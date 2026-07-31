import json
import os
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AIYouTubeKidsOS:
    def __init__(self, project_id):
        self.project_id = project_id
        self.state_dir = Path("./state")
        self.state_file = self.state_dir / f"{project_id}.json"
        self.outputs_dir = Path("./outputs")
        self.outputs_dir.mkdir(exist_ok=True)
        self.agents_dir = Path("./agents")
        self.knowledge_dir = Path("./knowledge")
        
        # Ensure state directory exists
        self.state_dir.mkdir(exist_ok=True)
        
        # Load or initialize state
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.state = json.load(f)
            logger.info(f"Loaded existing state for project {project_id}")
        else:
            self.state = self._initialize_state()
            self._save_state()
            logger.info(f"Initialized new state for project {project_id}")

        self.agent_prompts = self._load_agent_prompts()
        self.knowledge_base = self._load_knowledge_base()

    def _initialize_state(self):
        return {
            "project_id": self.project_id,
            "status": "active",
            "current_phase": 1,
            "metadata": {
                "created_at": "2026-07-31T12:00:00Z", # Placeholder, should use datetime.now()
                "updated_at": "2026-07-31T12:00:00Z",
                "assigned_character": "curious_robot",
                "target_language": "en"
            },
            "phases": {
                "phase_1_strategist": {"status": "pending", "output": None, "decision_matrix": None},
                "phase_2_researcher": {"status": "pending", "output": None, "decision_matrix": None},
                "phase_3_writer": {"status": "pending", "output": None, "decision_matrix": None},
                "phase_4_production": {"status": "pending", "output": None, "decision_matrix": None},
                "phase_5_seo": {"status": "pending", "output": None, "decision_matrix": None},
                "phase_6_analyst": {"status": "pending", "output": None, "decision_matrix": None}
            }
        }

    def _save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def _load_agent_prompts(self):
        prompts = {}
        for agent_file in self.agents_dir.glob("phase_*.md"):
            phase_name = agent_file.stem.replace("_system", "")
            with open(agent_file, 'r') as f:
                prompts[phase_name] = f.read()
        return prompts

    def _load_knowledge_base(self):
        knowledge = {}
        for kb_file in self.knowledge_dir.rglob("*.md"):
            relative_path = kb_file.relative_to(self.knowledge_dir)
            with open(kb_file, 'r') as f:
                knowledge[str(relative_path)] = f.read()
        return knowledge

    def _simulate_llm_call(self, system_prompt, user_input, phase_name):
        logger.info(f"Simulating LLM call for {phase_name}...")
        # In a real scenario, this would be an actual LLM API call.
        # For demonstration, we'll return a simple simulated output.
        if phase_name == "phase_1_strategist":
            return {
                "concept": "A friendly robot named Robo explores the solar system, learning about each planet.",
                "target_age_group": "4-6",
                "educational_goal": "Introduce planets and basic solar system facts",
                "unique_selling_point": "Interactive learning with a curious robot",
                "main_characters": [{"name": "Robo", "traits": "curious, friendly, metallic blue"}]
            }
        elif phase_name == "phase_2_researcher":
            prev_output = user_input # In a real scenario, this would be parsed
            return {
                "learning_objectives": ["Identify planets by name", "Understand basic size differences"],
                "attention_span_limit": "5-7 mins",
                "engagement_hooks": ["Robo asks questions", "Repetitive planet song"]
            }
        elif phase_name == "phase_3_writer":
            prev_output = user_input # In a real scenario, this would be parsed
            return {
                "character_bible": {"Robo": {"appearance": "metallic blue, round eyes", "personality": "curious"}},
                "script": [
                    {"scene": 1, "setting": "Robo's spaceship", "dialogue": "Hello, friends! Today we explore!", "action": "Robo waves"},
                    {"scene": 2, "setting": "Orbiting Earth", "dialogue": "Look, a blue planet!", "action": "Robo points"}
                ]
            }
        elif phase_name == "phase_4_production":
            prev_output = user_input # In a real scenario, this would be parsed
            return {
                "scene_1": {
                    "image_prompt": "3D Pixar-like, bright pastel colors, soft lighting, simple backgrounds. Robo, metallic blue, round eyes, waving in a spaceship cockpit.",
                    "video_prompt": "Robo waves slowly, then points to a window.",
                    "camera": "Wide Shot",
                    "actions_emotions": "Robo: happy, curious, waving arms",
                    "voice_sfx": "High-pitched, energetic voice. Spaceship hum, happy chime."
                },
                "scene_2": {
                    "image_prompt": "3D Pixar-like, bright pastel colors, soft lighting, simple backgrounds. Robo, metallic blue, round eyes, pointing at a blue planet outside the window.",
                    "video_prompt": "Robo points with one arm, then turns head to look at the planet.",
                    "camera": "Slow Push-in on Robo's face",
                    "actions_emotions": "Robo: amazed, pointing",
                    "voice_sfx": "Energetic voice. Twinkling sound effect."
                }
            }
        elif phase_name == "phase_5_seo":
            prev_output = user_input # In a real scenario, this would be parsed
            return {
                "titles": ["Robo's Space Adventure!", "Learn Planets with Robo!", "Kids Explore Solar System!"],
                "best_title": "Robo's Space Adventure!",
                "description": "Join Robo on an amazing journey through the solar system! Learn about planets, stars, and more in this fun educational video for kids. #KidsLearning #SolarSystem #Robo",
                "keywords": ["kids animation", "solar system", "planets", "learning for kids", "space adventure", "educational video"],
                "thumbnail_concept": "Robo's big, friendly face with Earth and Mars in the background, bright colors."
            }
        elif phase_name == "phase_6_analyst":
            prev_output = user_input # In a real scenario, this would be parsed
            return {
                "summary": "Initial performance good, but retention drops at scene 2.",
                "weaknesses": ["Scene 2 too long", "Not enough interaction"],
                "actionable_changes": ["Shorten Scene 2 dialogue", "Add a 'what do you see?' prompt in Scene 2"]
            }
        return {"simulated_output": f"Output for {phase_name} based on: {user_input}"}

    def run_phase(self, phase_num, user_topic="Solar System Exploration"):
        phase_map = {
            1: "phase_1_strategist",
            2: "phase_2_researcher",
            3: "phase_3_writer",
            4: "phase_4_production",
            5: "phase_5_seo",
            6: "phase_6_analyst",
        }
        phase_key = phase_map.get(phase_num)
        if not phase_key:
            logger.error(f"Invalid phase number: {phase_num}")
            return

        logger.info(f"Starting Phase {phase_num} ({phase_key})...")
        
        system_prompt = self.agent_prompts.get(phase_key)
        if not system_prompt:
            logger.error(f"System prompt not found for {phase_key}")
            return

        # Prepare user input for the current phase
        # For now, we'll pass the previous phase's output as user_input
        # In a real system, this would involve more sophisticated parsing and formatting
        previous_phase_output = None
        if phase_num > 1:
            prev_phase_key = phase_map.get(phase_num - 1)
            if prev_phase_key and self.state["phases"][prev_phase_key]["output"]:
                previous_phase_output = self.state["phases"][prev_phase_key]["output"]
        
        user_input = {"topic": user_topic, "previous_output": previous_phase_output}

        # Simulate LLM call
        phase_output = self._simulate_llm_call(system_prompt, user_input, phase_key)

        self.state["phases"][phase_key]["status"] = "completed"
        self.state["phases"][phase_key]["output"] = phase_output
        self.state["phases"][phase_key]["decision_matrix"] = {"score": 9.5} # Mock score
        
        self.state["current_phase"] = phase_num + 1
        self.state["metadata"]["updated_at"] = "2026-07-31T12:05:00Z" # Placeholder
        
        if phase_num == 6:
            self.state["status"] = "completed"
            
        self._save_state()
        logger.info(f"Phase {phase_num} ({phase_key}) completed.")

    def run_pipeline(self, user_topic="Solar System Exploration"):
        logger.info(f"Starting pipeline for project {self.project_id} with topic: {user_topic}")
        for phase_num in range(1, 7):
            phase_map = {
                1: "phase_1_strategist",
                2: "phase_2_researcher",
                3: "phase_3_writer",
                4: "phase_4_production",
                5: "phase_5_seo",
                6: "phase_6_analyst",
            }
            phase_key = phase_map.get(phase_num)

            if self.state["phases"][phase_key]["status"] == "pending":
                self.run_phase(phase_num, user_topic)
            else:
                logger.info(f"Phase {phase_num} ({phase_key}) already completed, skipping.")

if __name__ == "__main__":
    project_id = sys.argv[1] if len(sys.argv) > 1 else "default_project"
    topic = sys.argv[2] if len(sys.argv) > 2 else "Solar System Exploration"
    os_instance = AIYouTubeKidsOS(project_id)
    os_instance.run_pipeline(topic)
