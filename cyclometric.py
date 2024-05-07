import ast


class CyclomaticComplexity:
    def __init__(self, code):
        self.code = code

    def calculate_complexity(self):
        tree = ast.parse(self.code)
        complexity = 1  # Default complexity is 1 for a single entry point

        for node in ast.walk(tree):
            if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):
                # For each 'if', 'while', or 'for' statement, add 1 to the complexity
                complexity += 1
            elif isinstance(node, ast.Try) or isinstance(node, ast.ExceptHandler):
                # For each 'try' statement or 'except' block, add 1 to the complexity
                complexity += 1
            elif isinstance(node, ast.BoolOp) or isinstance(node, ast.BinOp) or \
                    isinstance(node, ast.Compare) or isinstance(node, ast.Call):
                # For boolean expressions, binary operations, function calls, etc., add 1 to the complexity
                complexity += 1
        return complexity


# Example usage
if __name__ == "__main__":
    filename = "code.txt"  # replace with your filename
    with open(filename, "r") as file:
        code_content = file.read()

    complexity_calculator = CyclomaticComplexity(code_content)
    complexity = complexity_calculator.calculate_complexity()
    print("Cyclomatic Complexity:", complexity)
