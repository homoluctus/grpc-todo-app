# grpc-todo-app
Todo app is used gRPC

## Component
- server
- client
- database (json file)

## Usage

```
$ python -m todo server todo_list.json &

$ python -m todo client
============ get_todo_list() ================
[task {
  id: 1
  name: "task1"
  is_complete: true
  priority: MED
}
, task {
  id: 2
  name: "task2"
  priority: HIGH
}
]
============ get_task_by_id() ================
id: 1
name: "task1"
is_complete: true
priority: MED

============ get_task_by_name() ================
id: 2
name: "task2"
priority: HIGH
```