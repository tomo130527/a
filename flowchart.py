import graphviz

def generate_flowchart(logic_str, filename="flowchart.png", show_code=False):
    """
    Generates a flow chart for the given program logic and saves it as an image file.
    
    Args:
        logic_str (str): A string representing the program logic in a specific format.
        filename (str, optional): The filename for the generated image. Default is "flowchart.png".
        show_code (bool, optional): Whether to include the code snippets in the flow chart. Default is False.
    
    Returns:
        None
    """
    
    # Create a new Graphviz graph object
    graph = graphviz.Digraph()
    graph.attr('node', shape='rectangle')
    
    # Split the logic string into lines
    lines = logic_str.strip().split('\n')
    
    # Keep track of the current node and its children
    current_node = None
    children = []
    
    # Iterate through each line and create nodes/edges
    for line in lines:
        line = line.strip()
        
        if line.startswith('->'):
            # This is a child node
            label = line[2:].strip()
            child_node = f"node{len(graph.body)}"
            graph.node(child_node, label)
            
            if current_node:
                # Connect the current node to the child node
                if label in ['True', 'False']:
                    # Use different edge styles for True and False branches
                    if label == 'True':
                        graph.edge(current_node, child_node, color='green')
                    else:
                        graph.edge(current_node, child_node, color='red')
                else:
                    graph.edge(current_node, child_node)
                
            children.append(child_node)
            
        else:
            # This is a parent node
            label = line
            if show_code:
                label = f"<{line}>"
            current_node = f"node{len(graph.body)}"
            graph.node(current_node, label)
            
            # Connect the current node to its children
            for child in children:
                graph.edge(current_node, child)
            
            children = []
    
    # Render the graph as an image file
    graph.render(filename, format="png", cleanup=True)
    print(f"Flow chart saved as {filename}")

# Example usage
logic_str = """
Start
-> Check if number is even
    -> True
        -> Print "Even"
    -> False
        -> Print "Odd"
End
"""

generate_flowchart(logic_str)

# Example with code snippets
logic_str = """
<num = int(input("Enter a number: "))>
-> <num % 2 == 0>
    -> True
        -> <print("Even")>
    -> False
        -> <print("Odd")>
<print("Done")>
"""

generate_flowchart(logic_str, show_code=True)