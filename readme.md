### 架构设计

```python
三层架构
    - 用户视图层：与用户交互
        - core
            src.py
    - 逻辑接口层：做核心的业务逻辑处理
        - interface
            - admin_interface.py
            - teacher_interface.py
            - student_interface.py
    - 数据处理层：用于数据的增删改查
        - db
            db_handler.py

```