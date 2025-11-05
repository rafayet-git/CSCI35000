"""
Meeting Scheduler - CSP Sprint Challenge
Difficulty: Hard
Interview companies: Microsoft, Airbnb, scheduling startups

Your task: Complete the constraint checking and backtracking solver
"""

class MeetingScheduler:
    def __init__(self, events, time_slots):
        """
        Initialize the scheduler
        
        Args:
            events: list of event names
            time_slots: list of time slot names
        """
        self.events = events
        self.time_slots = time_slots
        self.n_events = len(events)
        self.n_slots = len(time_slots)
        
        # Store constraints
        self.unavailable = {}  # {event: [unavailable_slots]}
        self.cannot_be_adjacent = []  # [(event1, event2), ...]
        self.must_be_in = {}  # {event: required_slot}
        
        # Solution: maps event index to slot index
        self.assignment = [-1] * self.n_events
    
    def add_unavailable_constraint(self, event, slot):
        """Event cannot be scheduled in this slot"""
        if event not in self.unavailable:
            self.unavailable[event] = []
        self.unavailable[event].append(slot)
    
    def add_adjacency_constraint(self, event1, event2):
        """These two events cannot be in adjacent time slots"""
        self.cannot_be_adjacent.append((event1, event2))
    
    def add_required_slot(self, event, slot):
        """Event must be in this specific slot"""
        self.must_be_in[event] = slot
    
    def is_valid_assignment(self, event_idx, slot_idx):
        """
        TODO: Implement this function!
        
        Check if assigning event_idx to slot_idx is valid
        
        Checks needed:
        1. Slot not already occupied by another event
        2. Event not in unavailable slots
        3. If event has required slot, must be that slot
        4. Event not adjacent to events it can't be adjacent to
        
        Args:
            event_idx: index of event in self.events
            slot_idx: index of slot in self.time_slots
        
        Returns:
            True if valid, False otherwise
        """
        event_name = self.events[event_idx]
        slot_name = self.time_slots[slot_idx]
        
        # TODO: Check if slot already occupied
        # Hint: loop through self.assignment, check if slot_idx already used
        
        
        # TODO: Check if event unavailable in this slot
        # Hint: check self.unavailable dictionary
        
        
        # TODO: Check if event has required slot
        # Hint: check self.must_be_in dictionary
        
        
        # TODO: Check adjacency constraints
        # Hint: for each (e1, e2) in self.cannot_be_adjacent,
        #       if one is current event and other is assigned,
        #       check if their slots are adjacent (differ by 1)
        
        
        return True  # Replace with your logic
    
    def solve(self, event_idx=0):
        """
        TODO: Implement this function!
        
        Backtracking solver for meeting scheduling
        
        Algorithm:
        1. Base case: if event_idx >= n_events, all events scheduled! Return True
        2. Try each time slot for current event:
           a. Check if assignment is valid (use is_valid_assignment)
           b. If valid, make assignment (self.assignment[event_idx] = slot_idx)
           c. Recursively try to schedule remaining events
           d. If recursive call succeeds, return True
           e. If fails, BACKTRACK (self.assignment[event_idx] = -1)
        3. If all slots tried and none worked, return False
        
        Args:
            event_idx: current event index we're trying to schedule
        
        Returns:
            True if solution found, False otherwise
        """
        
        # TODO: Base case
        
        
        # TODO: Try each time slot
        
        
        # TODO: If no slot worked, return False
        
        
        pass  # Remove when you implement
    
    def print_schedule(self):
        """Print the schedule in a nice format"""
        if -1 in self.assignment:
            print("No valid schedule found!")
            return
        
        print("\nSchedule:")
        print("=" * 50)
        for i, event in enumerate(self.events):
            slot_idx = self.assignment[i]
            slot_name = self.time_slots[slot_idx]
            print(f"{slot_name:15} | {event}")
        print("=" * 50)
    
    def get_schedule_dict(self):
        """Returns schedule as dictionary"""
        return {
            self.events[i]: self.time_slots[self.assignment[i]]
            for i in range(self.n_events)
            if self.assignment[i] != -1
        }

# Test Case 1: Simple scheduling
def test_simple():
    print("Test 1: Simple Scheduling")
    print("=" * 50)
    
    events = ["Talk A", "Talk B", "Talk C"]
    slots = ["9am", "10am", "11am", "1pm"]
    
    scheduler = MeetingScheduler(events, slots)
    
    # Constraints
    scheduler.add_unavailable_constraint("Talk A", "9am")
    scheduler.add_adjacency_constraint("Talk B", "Talk C")
    scheduler.add_required_slot("Talk C", "1pm")
    
    print("Events:", events)
    print("Time slots:", slots)
    print("\nConstraints:")
    print("- Talk A cannot be at 9am")
    print("- Talk B and Talk C cannot be adjacent")
    print("- Talk C must be at 1pm")
    
    if scheduler.solve():
        scheduler.print_schedule()
    else:
        print("\nNo solution found!")

# Test Case 2: Conference scheduling
def test_conference():
    print("\n\nTest 2: Conference Scheduling")
    print("=" * 50)
    
    events = [
        "Keynote",
        "AI Workshop",
        "Lunch Break",
        "Panel Discussion",
        "Networking"
    ]
    
    slots = [
        "9:00-10:00",
        "10:00-11:00",
        "11:00-12:00",
        "12:00-1:00",
        "1:00-2:00",
        "2:00-3:00"
    ]
    
    scheduler = MeetingScheduler(events, slots)
    
    # Constraints
    scheduler.add_required_slot("Keynote", "9:00-10:00")  # Keynote first
    scheduler.add_required_slot("Lunch Break", "12:00-1:00")  # Lunch at noon
    scheduler.add_unavailable_constraint("Panel Discussion", "9:00-10:00")  # Panel not morning
    scheduler.add_adjacency_constraint("AI Workshop", "Panel Discussion")  # Need break between
    
    print("Events:", events)
    print("Time slots:", slots)
    print("\nConstraints:")
    print("- Keynote must be at 9:00-10:00")
    print("- Lunch Break must be at 12:00-1:00")
    print("- Panel Discussion cannot be at 9:00-10:00")
    print("- AI Workshop and Panel Discussion cannot be adjacent")
    
    if scheduler.solve():
        scheduler.print_schedule()
    else:
        print("\nNo solution found!")

# Test Case 3: Impossible schedule
def test_impossible():
    print("\n\nTest 3: Impossible Schedule")
    print("=" * 50)
    
    events = ["Event A", "Event B"]
    slots = ["Morning", "Afternoon"]
    
    scheduler = MeetingScheduler(events, slots)
    
    # Make it impossible
    scheduler.add_required_slot("Event A", "Morning")
    scheduler.add_required_slot("Event B", "Morning")  # Both want same slot!
    
    print("Events:", events)
    print("Time slots:", slots)
    print("\nConstraints:")
    print("- Event A must be in Morning")
    print("- Event B must be in Morning")
    print("(This should be impossible!)")
    
    if scheduler.solve():
        scheduler.print_schedule()
    else:
        print("\nNo solution found! (Expected - constraints are impossible)")

if __name__ == "__main__":
    test_simple()
    test_conference()
    test_impossible()

"""
Expected output for Test 1:
Schedule:
================================================
10am            | Talk A
9am             | Talk B
1pm             | Talk C
================================================
(or another valid solution)

Expected output for Test 2:
Schedule:
================================================
9:00-10:00      | Keynote
10:00-11:00     | AI Workshop
11:00-12:00     | (could be Networking or Panel)
12:00-1:00      | Lunch Break
1:00-2:00       | (one of the remaining)
2:00-3:00       | (one of the remaining)
================================================

Expected output for Test 3:
No solution found! (Expected - constraints are impossible)
"""
