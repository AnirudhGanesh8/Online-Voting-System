users={}
voters=[]
candidates=[]
vote_records=[]
login_status=False


def login(voter_id,password):
    
    if voter_id in users and users[voter_id]==password:
        print("Successfully Logged in!")
        return True
    else:
        print("Please register before you login")
        return False

class Voter:
    def __init__(self,voter_id,name,age,hasVoted=False):
        self.voter_id=voter_id
        self.name=name
        self.age=age
        self.hasVoted=hasVoted
    
    def authenticate(self,voter_id,password):
        if login(voter_id,password):
            return True
        else:
            return False

    def castVote(self,candidate):
        if not self.hasVoted:
            candidate.incrementVote()
            self.hasVoted=True
            print(f"{self.name} has voted for {candidate.name}")
        else:
            print(f"{self.name} has already voted and cannot vote again")

    def getStatus(self):
        return f"Voter ID: {self.voter_id},Name:{self.name},Age:{self.age},Voted:{self.hasVoted}"

class Candidate:
    def __init__(self,candidate_id,name,party,vote_count=0):
        self.candidate_id=candidate_id
        self.name=name
        self.party=party
        self.vote_count=vote_count

    def register_candidates(self,candidate_id,candidate_name,candidate_party,candidates):
        candidate_id=input("Enter the candidate ID:")
        candidate_name=input("Enter the candidate name:")
        candidate_party=input("Enter the candidate party:")
        candidates.append(Candidate(candidate_id,candidate_name,candidate_party))

    def incrementVote(self):
        self.vote_count += 1

    def getDetails(self):
        return f"Candidate ID: {self.candidate_id}, Name: {self.name}, Party: {self.party}, Vote Count: {self.vote_count}"

class Election:
    def __init__(self,election_id,title,startDate,endDate,status):
        self.election_id=election_id
        self.title=title
        self.startDate=startDate
        self.endDate=endDate
        self.status=status

    def addCandidate(self,candidate_id,candidate_name,candidate_party,candidates):
        candidate_id=input("Enter the candidate ID:")
        candidate_name=input("Enter the candidate name:")
        candidate_party=input("Enter the candidate party:")
        candidates.append(Candidate(candidate_id,candidate_name,candidate_party))
        
    def closeElection(self):
        self.status="Closed"
        print("Election is now closed")

    def declareResults(self,candidates):
        print(f"Results for Election: {self.title}")
        for candidate in candidates:
            print(candidate.getDetails())
class VoteRecord:
    def __init__(self, recordId,voterId,electionID,timestamp):
        self.recordId=recordId
        self.voterId=voterId
        self.electionID=electionID
        self.timestamp=timestamp
    
    def validate(self,voterId,electionID):
        for record in vote_records:
            if record.voterId==voterId and record.electionID==electionID:
                return False
        return True
    
    def save(self):
        vote_records.append(self)

class VotingSystem:
    def __init__(self,elections,voters):
        self.users={}
        self.voters=[]
        self.candidates=[]
        self.elections=[]
        self.vote_records=[]
        self.login_status=False
    
    def createElection(self,election_id,title,startDate,endDate,status):
        self.elections.append(Election(election_id,title,startDate,endDate,status))
    
    def registerVoter(self,voter_id,password,name,age):
        if voter_id in self.users:
            print("Already Registered - Go to Login")
        else:
            self.users[voter_id]=password
            self.voters.append(Voter(voter_id,name,age))

    def getResults(self,election_id):
        for election in self.elections:
            if election.election_id==election_id:
                election.declareResults(self.candidates)
        print("Election not found")

class Main:
    voting_system = VotingSystem([],[])

    while True:
        print("\nAdmin Menu")
        print("1.Create election")
        print("2.Register voter")
        print("3.Add candidate")
        print("4.Close election")
        print("5.Show results")
        print("6.Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            election_id=input("Enter the election ID:")
            title=input("Enter the election title:")
            startDate=input("Enter the election start date (YYYY-MM-DD):")
            endDate=input("Enter the election end date:")
            status="Open"
            voting_system.createElection(election_id,title,startDate,endDate,status)
            
        elif choice == '2':
            voter_id=input("Enter the voter ID:")
            password=input("Enter the password:")
            name=input("Enter the voter name:")
            age=int(input("Enter the voter age:"))
            if age < 18:
                print("Registration failed: you must be 18 or older to register as a voter.")
            else:
                voting_system.registerVoter(voter_id,password,name,age)

        elif choice == '3':
            candidate_id=input("Enter the candidate ID:")
            candidate_name=input("Enter the candidate name:")
            candidate_party=input("Enter the candidate party:")
            voting_system.candidates.append(Candidate(candidate_id,candidate_name,candidate_party))

        elif choice == '4':
            election_id=input("Enter the election ID to close:")
            for election in voting_system.elections:
                if election.election_id==election_id:
                    election.closeElection()
                    break
                
        elif choice == '5':
            election_id=input("Enter the election ID to view results:")
            voting_system.getResults(election_id)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
