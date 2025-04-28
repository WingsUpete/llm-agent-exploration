from pydantic import BaseModel, Field

class Node(BaseModel):
  """
  Represents a node in a graph with associated properties.
  """
  id: str = Field(description='A unique identifier for the node.')
  type: str = Field('Node', description='Type/Label of the node, default is "Node".')
  properties: dict = Field(default_factory=dict, description='Additional properties and metadata associated with the node.')


class Relationship(BaseModel):
  """
  Represents a directed relationship between two nodes in a graph.
  """
  source: Node = Field(description='Source node of the relationship.')
  target: Node = Field(description='Target node of the relationship.')
  type: str = Field(description='Type of the relationship.')
  properties: dict = Field(default_factory=dict, description='Additional properties associated with the relationship.')


class KnowledgeGraph(BaseModel):
  """
  Represents a knowledge graph consisting of nodes and relationships.
  """
  nodes: list[Node] = Field(description='List of nodes in the graph.')
  relationships: list[Relationship] = Field(description='List of relationships in the graph.')


if __name__ == '__main__':
  import json
  print(json.dumps(KnowledgeGraph.model_json_schema(), indent=2))