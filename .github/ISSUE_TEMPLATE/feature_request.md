name: Feature request
description: Suggest a capability for the runbook, validator or stage toolkit
title: "[feat] "
labels: enhancement
body:
  - type: textarea
    id: problem
    attributes:
      label: Проблема
      description: Что невозможно или неудобно делать сейчас.
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Предлагаемое решение
    validations:
      required: true
  - type: textarea
    id: customer_value
    attributes:
      label: Ценность для проекта
      description: |
        Какую задачу в runbook'е это разблокирует.
        Правило проекта: ценность формулируется через проверяемый исход,
        а не через количество функций.
    validations:
      required: true
  - type: checkboxes
    id: gates
    attributes:
      label: Гейты
      options:
        - label: Не меняет публичные контракты
          required: false
        - label: Требует ADR
          required: false
        - label: Затрагивает P0 scope
          required: false
