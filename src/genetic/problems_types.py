from enum import Enum, auto

class ProblemType(Enum):
    MINIMIZE = auto()
    MAXIMIZE = auto()
    FEASIBILITY = auto()
    MULTI_OBJECTIVE = auto()
    STOCHASTIC = auto()
    DYNAMIC = auto()
    COMBINATORIAL = auto()

    def description(self):
        descriptions = {
            ProblemType.MINIMIZE: "Minimize the objective function.",
            ProblemType.MAXIMIZE: "Maximize the objective function.",
            ProblemType.FEASIBILITY: "Find any solution that satisfies all constraints.",
            ProblemType.MULTI_OBJECTIVE: "Optimize multiple objectives simultaneously, often involving trade-offs.",
            ProblemType.STOCHASTIC: "Optimize expected outcomes considering randomness or uncertainty.",
            ProblemType.DYNAMIC: "Optimize problems where the objective function, constraints, or both change over time.",
            ProblemType.COMBINATORIAL: "Find the best combination or sequence from a discrete set of elements."
        }
        return descriptions.get(self, "Unknown optimization type.")

    @property
    def action(self):
        """Returns a verb describing the optimization action."""
        return self.name.lower()


class ProblemDataType(Enum):
    INTEGER = auto()
    REAL = auto()
    CATEGORICAL = auto()
    COMBINATION = auto()
    BINARY = auto()
    SEQUENTIAL = auto()

    def description(self):
        descriptions = {
            ProblemDataType.INTEGER: "Integer values only.",
            ProblemDataType.REAL: "Real (continuous) values.",
            ProblemDataType.CATEGORICAL: "Categorical (discrete) values.",
            ProblemDataType.COMBINATION: "Combination of integer, real, and/or categorical values.",
            ProblemDataType.BINARY: "Binary values only, typically 0 or 1.",
            ProblemDataType.SEQUENTIAL: "Data structured in sequences or time series.",
        }
        return descriptions.get(self, "Unknown data type.")

    @property
    def data_type(self):
        """Returns a simple string representing the data type."""
        return self.name.lower()