import os


class VirtualFileSystem:
    def __init__(self, physical_path: str | None = None):
        if physical_path:
            self.root = physical_path
            os.makedirs(physical_path, exist_ok=True)
        else:
            self.root = os.getcwd()

    def list_dir(self, path: str = ".") -> list[str]:
        full_path = os.path.join(self.root, path)
        if not os.path.exists(full_path):
            return []
        return os.listdir(full_path)

    def change_dir(self, path: str) -> bool:
        full_path = os.path.join(self.root, path)
        if os.path.exists(full_path) and os.path.isdir(full_path):
            self.root = full_path
            return True
        return False

    def get_current_dir(self) -> str:
        return self.root