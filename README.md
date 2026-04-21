# my_own_namespace.yandex_cloud_elk

Модуль `my_own_module` создаёт текстовый файл на удалённом хосте.

## Параметры модуля
- `path` (str, required): путь к файлу
- `content` (str, required): содержимое

## Роль `write_file`
Переменные:
- `file_path` (default: /tmp/default.txt)
- `file_content` (default: "Default content")

## Пример playbook
```yaml
- hosts: all
  roles:
    - my_own_namespace.yandex_cloud_elk.write_file
