class MilestoneManager:
    def __init__(self):
        self.milestones = []

    def create_milestone(self, description):
        """
        Creates a new milestone.
        :param description: Description of the milestone.
        """
        self.milestones.append({'description': description, 'completed': False})
        print(f"New milestone created: {description}")

    def submit_milestones(self):
        """
        Submits the milestone checklist.
        """
        print("Milestone checklist submitted")

    def complete_milestone(self, description):
        """
        Marks a milestone as completed.
        :param description: Description of the completed milestone.
        """
        for milestone in self.milestones:
            if milestone['description'] == description:
                milestone['completed'] = True
                print(f"Milestone completed: {description}")
                return
        print(f"Milestone '{description}' not found")

    def verify_milestone(self, description):
        """
        Verifies the completion of a milestone.
        :param description: Description of the milestone to verify.
        """
        for milestone in self.milestones:
            if milestone['description'] == description:
                if milestone['completed']:
                    print(f"Milestone verified: {description}")
                else:
                    print(f"Milestone '{description}' is not completed")
                return
        print(f"Milestone '{description}' not found")
