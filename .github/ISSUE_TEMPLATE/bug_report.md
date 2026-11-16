name: Bug report
description: Something in the runbook tooling or artifacts does not behave as specified
title: "[bug] "
labels: bug
body:
  - type: markdown
    attributes:
      value: |
        Спасибо за баг-репорт. Проверьте, пожалуйста, воспроизводится ли он
        на свежем `main`.
  - type: textarea
    id: symptom
    attributes:
      label: Что наблюдается
      description: Ожидаемое поведение и фактическое.
      placeholder: |
        Ожидалось: `python tools/runbook_validate.py --stage STAGE-00` → PASS
        Фактически: FAIL с причиной ...
    validations:
      required: true
  - type: textarea
    id: repro
    attributes:
      label: Шаги воспроизведения
      value: |
        1. Клонировать репозиторий
        2. ...
        3. ...
    validations:
      required: true
  - type: input
    id: env
    attributes:
      label: Окружение
      value: |
        OS: Windows 11
        Python: 3.13.0
        ruff: 0.14.13
        pytest: 9.0.3
  - type: textarea
    id: logs
    attributes:
      label: Вывод команды
      render: shell
