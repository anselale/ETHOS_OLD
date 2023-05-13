from Agents.Func.agent_functions import AgentFunctions
from Logs.logger_config import Logger

logger = Logger(name="Search Agent")


class SearchAgent:
    agent_data = None
    agent_funcs = None
    storage = None

    def __init__(self):
        self.agent_funcs = AgentFunctions('SearchAgent')
        self.agent_data = self.agent_funcs.agent_data
        self.storage = self.agent_data['storage'].storage_utils
        logger.set_level('debug')

    def run_agent(self, text, feedback=None):
        logger.log(f"Running Agent...", 'info')

        data = self.load_data_from_storage()

        prompt_formats = self.get_prompt_formats(data)

        prompt = self.generate_prompt(prompt_formats, feedback)

        with self.agent_funcs.thinking():
            result = self.execute_task(prompt)

        self.save_results(result)

        self.agent_funcs.stop_thinking()

        self.agent_funcs.print_result(result)

        logger.log(f"Agent Done!", 'info')

    def load_data_from_storage(self):
        # Load necessary data from storage and return it as a dictionary
        pass

    def get_prompt_formats(self, data):
        # Create a dictionary of prompt formats based on the loaded data
        prompt_formats = {
            'SystemPrompt': {'objective': self.agent_data['objective']},
            'ContextPrompt': {'context': data['context']},
            'InstructionPrompt': {'task': data['task']}
        }
        return prompt_formats
    pass

    def generate_prompt(self, prompt_formats, feedback=None):
        # Generate the prompt using prompt_formats and return it.
        system_prompt = self.agent_data['prompts']['SystemPrompt']
        context_prompt = self.agent_data['prompts']['ContextPrompt']
        instruction_prompt = self.agent_data['prompts']['InstructionPrompt']
        feedback_prompt = self.agent_data['prompts']['FeedbackPrompt'] if feedback != "" else ""

        # Format Prompts
        system_prompt = system_prompt.format(**prompt_formats.get('SystemPrompt', {}))
        context_prompt = context_prompt.format(**prompt_formats.get('ContextPrompt', {}))
        instruction_prompt = instruction_prompt.format(**prompt_formats.get('InstructionPrompt', {}))
        feedback_prompt = feedback_prompt.format(feedback=feedback)

        prompt = [
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{context_prompt}{instruction_prompt}{feedback_prompt}"}
        ]

        return prompt
        pass

    def execute_task(self, prompt):
        # Execute the main task of the agent and return the result
        pass

    def save_results(self, result):
        # Save the results to storage
        pass

