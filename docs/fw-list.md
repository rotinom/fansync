```
{
  "FAN-FDR2L0": {
    "timestamp": 1683618254000,
    "size": 10527,
    "lastModified": 1683618254000,
    "name": "FDR2L0_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ]
      },
      "familyMembers": [
        ".*-FDR2L0$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "a7c822f1-8940-4ac5-8393-81c88f8178af"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR2L0 FAN"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L0 FAN"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR2L0-thumbnail-1625456887"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR2L0",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_LEARN_LOAD": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.FAN_LEARN_LOAD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION"
        ]
      }
    }
  },
  "FAN-FAR1L1": {
    "timestamp": 1683618152000,
    "size": 12493,
    "lastModified": 1683618152000,
    "name": "FAR1L1_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FAR1L1$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync-FAR1L1 LIGHT"
          },
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FAR1L1 FAN"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L1/UAR1L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L1/UAR1L1 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FAR1L1-thumbnail-1545042970"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FAR1L1",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "toggle",
          "models": [
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "LIGHT-L2": {
    "timestamp": 1525085439375,
    "size": 6966,
    "lastModified": 1524798371200,
    "name": "L2_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "LIGHT_POWER_AND_DIMMER"
        ]
      },
      "familyMembers": [
        ".*-L2$"
      ],
      "integration": {
        "traits": [
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "brightness": {
                "max": 100,
                "min": 1,
                "key": "H02",
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Satellite MR101W-L2 Light"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Satellite Home Shield"
          }
        ]
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "L",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "text": "Parameter error",
              "value": 250
            },
            {
              "text": "Parameter length error",
              "value": 251
            },
            {
              "text": "Memory allocate failed",
              "value": 252
            },
            {
              "text": "Send error",
              "value": 253
            },
            {
              "text": "Unknown commands",
              "value": 254
            },
            {
              "text": "Unknown fields",
              "value": 255
            },
            {
              "text": "Too many entries",
              "value": 256
            },
            {
              "text": "Under voltage",
              "value": 257
            },
            {
              "text": "Over voltage",
              "value": 258
            },
            {
              "text": "Over current",
              "value": 259
            },
            {
              "text": "Under speed",
              "value": 260
            },
            {
              "text": "Over speed",
              "value": 261
            },
            {
              "text": "Stalled fault",
              "value": 262
            },
            {
              "text": "Open phase fault",
              "value": 263
            },
            {
              "text": "Chase max speed",
              "value": 264
            },
            {
              "text": "Over temperature",
              "value": 265
            },
            {
              "text": "EEPROM error",
              "value": 266
            },
            {
              "text": "Remote control did not learn",
              "value": 267
            },
            {
              "text": "Driver IC not response",
              "value": 268
            },
            {
              "text": "ACZ abnormal",
              "value": 269
            }
          ]
        }
      ],
      "familyName": "LIGHT-L2",
      "components": {
        "LIGHT_TURN_ON_TIMER": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H04"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.TURN_ON_TIMER",
          "hideFromGroup": true
        },
        "LIGHT_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "text": "INFORMATION_MODEL.OFF",
                  "value": 0
                },
                {
                  "text": "INFORMATION_MODEL.ON",
                  "value": 1
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "LIGHT_POWER_AND_DIMMER": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "func": "brightness",
                "min": 1,
                "step": 1
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "text": "INFORMATION_MODEL.OFF",
                  "value": 0
                },
                {
                  "text": "INFORMATION_MODEL.ON",
                  "value": 1
                }
              ]
            }
          ],
          "title": ""
        },
        "LIGHT_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "text": "INFORMATION_MODEL.OFF",
                  "value": 0
                },
                {
                  "text": "INFORMATION_MODEL.ON",
                  "value": 1
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "LIGHT_TURN_OFF_TIMER": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.TURN_OFF_TIMER",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "LIGHT_POWER_AND_DIMMER"
        ],
        "secondary": [
          "LIGHT_HOME_SHIELD",
          "LIGHT_TURN_OFF_TIMER",
          "LIGHT_TURN_ON_TIMER"
        ]
      }
    }
  },
  "FAN-FDR1L3": {
    "timestamp": 1683618259000,
    "size": 14994,
    "lastModified": 1683618259000,
    "name": "FDR1L3_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT"
        ]
      },
      "familyMembers": [
        ".*-FDR1L3$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR1L3 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "color_temperature": {
                "max": 5000,
                "key": "H04",
                "min": 3000,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR1L3 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR1L3 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR1L3-thumbnail-1578973500"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter?error"
            },
            {
              "value": 251,
              "text": "Parameter?length?error"
            },
            {
              "value": 252,
              "text": "Memory?allocate?failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR1L3",
      "components": {
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_LIGHT_CCT": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": [
                {
                  "value": 3000,
                  "text": "INFORMATION_MODEL.WARM"
                },
                {
                  "value": 4000,
                  "text": "INFORMATION_MODEL.NATURALWHITE"
                },
                {
                  "value": 5000,
                  "text": "INFORMATION_MODEL.COOL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT_CCT"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR1L1": {
    "timestamp": 1683618274000,
    "size": 12596,
    "lastModified": 1683618274000,
    "name": "FDR1L1_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR1L1$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR1L1 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync-FDR1L1 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR1L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR1L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FDR1L1 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR1L1-thumbnail-1545043557"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR1L1",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "toggle",
          "models": [
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FAR1L3_UAR1L3": {
    "timestamp": 1683618144000,
    "size": 14902,
    "lastModified": 1683618144000,
    "name": "FAR1L3_UAR1L3_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT"
        ]
      },
      "familyMembers": [
        ".*-FAR1L3$",
        ".*-UAR1L3$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "color_temperature": {
                "max": 5000,
                "key": "H04",
                "min": 3000,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FAR1L3/UAR1L3 LIGHT"
          },
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FAR1L3/UAR1L3 FAN"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L3/UAR1L3 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FAR1L3_UAR1L3-thumbnail-1578973509"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FAR1L3_UAR1L3",
      "components": {
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_LIGHT_CCT": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": [
                {
                  "value": 3000,
                  "text": "INFORMATION_MODEL.WARM"
                },
                {
                  "value": 4000,
                  "text": "INFORMATION_MODEL.NATURALWHITE"
                },
                {
                  "value": 5000,
                  "text": "INFORMATION_MODEL.COOL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT_CCT"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FAR1L2_UAR1L2": {
    "timestamp": 1683618133000,
    "size": 13830,
    "lastModified": 1683618133000,
    "name": "FAR1L2_UAR1L2_fan_type.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FAR1L2$",
        ".*-UAR1L2$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          },
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FAR1L2_UAR1L2-thumbnail-1544519684"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter?error"
            },
            {
              "value": 251,
              "text": "Parameter?length?error"
            },
            {
              "value": 252,
              "text": "Memory?allocate?failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FAR1L2_UAR1L2",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR1L2": {
    "timestamp": 1683618267000,
    "size": 13934,
    "lastModified": 1683618267000,
    "name": "FDR1L2_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR1L2$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR1L2 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR1L2 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR1L2-thumbnail-1544519703"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR1L2",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR1L0": {
    "timestamp": 1683618283000,
    "size": 10036,
    "lastModified": 1683618283000,
    "name": "FDR1L0_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ]
      },
      "familyMembers": [
        ".*-FDR1L0$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "a7c822f1-8940-4ac5-8393-81c88f8178af"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR1L0 FAN"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR1L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR1L0-thumbnail-1544519696"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR1L0",
      "components": {
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION"
        ]
      }
    }
  },
  "FAN-FDR2L3": {
    "timestamp": 1683618235000,
    "size": 15497,
    "lastModified": 1683618235000,
    "name": "FDR2L3_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT"
        ]
      },
      "familyMembers": [
        ".*-FDR2L3$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR2L3 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "color_temperature": {
                "max": 5000,
                "key": "H04",
                "min": 3000,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR2L3 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L3 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR2L3-thumbnail-1578974654"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR2L3",
      "components": {
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_LEARN_LOAD": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.FAN_LEARN_LOAD",
          "hideFromGroup": true
        },
        "FAN_LIGHT_CCT": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": [
                {
                  "value": 3000,
                  "text": "INFORMATION_MODEL.WARM"
                },
                {
                  "value": 4000,
                  "text": "INFORMATION_MODEL.NATURALWHITE"
                },
                {
                  "value": 5000,
                  "text": "INFORMATION_MODEL.COOL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT_CCT"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "LIGHT-L1": {
    "timestamp": 1525085434222,
    "size": 5064,
    "lastModified": 1524798371173,
    "name": "L1_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "LIGHT_POWER"
        ]
      },
      "familyMembers": [
        ".*-L1$"
      ],
      "integration": {
        "traits": [
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Satellite MR101W-L1 Light"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Satellite Home Shield"
          }
        ]
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        }
      ],
      "deviceId": "L",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "text": "Parameter error",
              "value": 250
            },
            {
              "text": "Parameter length error",
              "value": 251
            },
            {
              "text": "Memory allocate failed",
              "value": 252
            },
            {
              "text": "Send error",
              "value": 253
            },
            {
              "text": "Unknown commands",
              "value": 254
            },
            {
              "text": "Unknown fields",
              "value": 255
            },
            {
              "text": "Too many entries",
              "value": 256
            },
            {
              "text": "Under voltage",
              "value": 257
            },
            {
              "text": "Over voltage",
              "value": 258
            },
            {
              "text": "Over current",
              "value": 259
            },
            {
              "text": "Under speed",
              "value": 260
            },
            {
              "text": "Over speed",
              "value": 261
            },
            {
              "text": "Stalled fault",
              "value": 262
            },
            {
              "text": "Open phase fault",
              "value": 263
            },
            {
              "text": "Chase max speed",
              "value": 264
            },
            {
              "text": "Over temperature",
              "value": 265
            },
            {
              "text": "EEPROM error",
              "value": 266
            },
            {
              "text": "Remote control did not learn",
              "value": 267
            },
            {
              "text": "Driver IC not response",
              "value": 268
            },
            {
              "text": "ACZ abnormal",
              "value": 269
            }
          ]
        }
      ],
      "familyName": "LIGHT-L1",
      "components": {
        "LIGHT_TURN_ON_TIMER": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H04"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.TURN_ON_TIMER",
          "hideFromGroup": true
        },
        "LIGHT_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "text": "INFORMATION_MODEL.OFF",
                  "value": 0
                },
                {
                  "text": "INFORMATION_MODEL.ON",
                  "value": 1
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "LIGHT_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "text": "INFORMATION_MODEL.OFF",
                  "value": 0
                },
                {
                  "text": "INFORMATION_MODEL.ON",
                  "value": 1
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "LIGHT_TURN_OFF_TIMER": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.TURN_OFF_TIMER",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "LIGHT_POWER"
        ],
        "secondary": [
          "LIGHT_HOME_SHIELD",
          "LIGHT_TURN_OFF_TIMER",
          "LIGHT_TURN_ON_TIMER"
        ]
      }
    }
  },
  "FAN-FDR2L2": {
    "timestamp": 1683618242000,
    "size": 14423,
    "lastModified": 1683618242000,
    "name": "FDR2L2_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR2L2$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR2L2 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR2L2 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FDR2L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR2L2-thumbnail-1625456905"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR2L2",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_LEARN_LOAD": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.FAN_LEARN_LOAD",
          "hideFromGroup": true
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR0L3_FAR0L3": {
    "timestamp": 1683618289000,
    "size": 14866,
    "lastModified": 1683618289000,
    "name": "FDR0L3_FAR0L3_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT"
        ]
      },
      "familyMembers": [
        ".*-FDR0L3$",
        ".*-FAR0L3$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR0L3/FAR0L3 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "color_temperature": {
                "max": 5000,
                "key": "H04",
                "min": 3000,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR0L3/FAR0L3 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR0L3/FAR0L3 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L2/UAR1L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR0L3_FAR0L3-thumbnail-1578973520"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR0L3_FAR0L3",
      "components": {
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_LIGHT_CCT": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H04",
              "values": [
                {
                  "value": 3000,
                  "text": "INFORMATION_MODEL.WARM"
                },
                {
                  "value": 4000,
                  "text": "INFORMATION_MODEL.NATURALWHITE"
                },
                {
                  "value": 5000,
                  "text": "INFORMATION_MODEL.COOL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT_CCT"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_LIGHT",
          "FAN_LIGHT_CCT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR0L2_FAR0L2": {
    "timestamp": 1683618295000,
    "size": 13829,
    "lastModified": 1683618295000,
    "name": "FDR0L2_FAR0L2_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR0L2$",
        ".*-FAR0L2$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR0L2/FAR0L2 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "light",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              },
              "brightness": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              }
            },
            "description": "Fanimation fanSync-FDR0L2/FAR0L2 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR0L2/FAR0L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR0L2/UAR0L2 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR0L2/UAR0L2 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR0L2_FAR0L2-thumbnail-1545043183"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 20,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H0C"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_brightness_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H0C"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR0L2_FAR0L2",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "range-with-toggle",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H0B"
                    }
                  ]
                }
              ],
              "key": "H0C",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "brightness"
              }
            },
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FAR1L0": {
    "timestamp": 1683618158000,
    "size": 10523,
    "lastModified": 1683618158000,
    "name": "FAR1L0_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ]
      },
      "familyMembers": [
        ".*-FAR1L0$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " FAN",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FAR1L0 FAN"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR1L0/UAR1L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR1L0/UAR1L0 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FAR1L0-thumbnail-1545042963"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FAR1L0",
      "components": {
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "values": [
                {
                  "value": 2,
                  "text": "INFORMATION_MODEL.CHANGE_DIRECTION"
                }
              ],
              "dependency": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 2,
                      "key": "H06"
                    }
                  ],
                  "result": {
                    "values": [
                      {
                        "value": 2,
                        "text": "INFORMATION_MODEL.REVERSING"
                      }
                    ]
                  }
                }
              ],
              "key": "H06"
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION"
        ]
      }
    }
  },
  "FAN-FDR0L1_FAR0L1": {
    "timestamp": 1683618300000,
    "size": 11521,
    "lastModified": 1683618300000,
    "name": "FDR0L1_FAR0L1_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR0L1$",
        ".*-FAR0L1$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR0L1/FAR0L1 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync-FDR0L1/FAR0L1 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR0L1/FAR0L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FAR0L1/UAR0L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FAR0L1/UAR0L1 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR0L1_FAR0L1-thumbnail-1545043550"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR0L1_FAR0L1",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_LIGHT": {
          "type": "toggle",
          "models": [
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR2L1": {
    "timestamp": 1683618248000,
    "size": 13133,
    "lastModified": 1683618248000,
    "name": "FDR2L1_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED",
          "FAN_LIGHT"
        ]
      },
      "familyMembers": [
        ".*-FDR2L1$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "0cf4dbb5-1fa9-4c85-8fc5-6d2f3adf7389"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR2L1 FAN"
          },
          {
            "append_name": " Light",
            "id": "LIGHT",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0B",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync-FDR2L1 LIGHT"
          },
          {
            "append_name": " Home Shield",
            "id": "HOME_SHIELD",
            "type": "switch",
            "attributes": {
              "on_off": {
                "key": "H0D",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "description": "Fanimation fanSync Home Shield"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 25
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 50
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 75
                  },
                  {
                    "speed_name": "boost",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "boost",
                          "speed 4"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 25,
                  "2": 50,
                  "3": 75,
                  "4": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": {
                    "range": [
                      0,
                      0
                    ]
                  },
                  "1": {
                    "range": [
                      1,
                      25
                    ]
                  },
                  "2": {
                    "range": [
                      26,
                      50
                    ]
                  },
                  "3": {
                    "range": [
                      51,
                      75
                    ]
                  },
                  "4": {
                    "range": [
                      76,
                      100
                    ]
                  }
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR2L1 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FDR2L1 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR2L1-thumbnail-1625456896"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "light_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H0B"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR2L1",
      "components": {
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_DIRECTION": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H06",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.FORWARD"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.REVERSE"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_DIRECTION"
        },
        "FAN_LIGHT": {
          "type": "toggle",
          "models": [
            {
              "key": "H0B",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.LIGHT"
        },
        "FAN_LEARN_LOAD": {
          "type": "text",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H05"
                    }
                  ]
                }
              ],
              "key": "H05",
              "values": {
                "func": "timer"
              }
            }
          ],
          "title": "INFORMATION_MODEL.FAN_LEARN_LOAD",
          "hideFromGroup": true
        },
        "FAN_HOME_SHIELD": {
          "type": "toggle",
          "models": [
            {
              "key": "H0D",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.HOME_SHIELD",
          "hideFromGroup": true
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": {
                "max": 100,
                "step": 1,
                "min": 1,
                "func": "fanSpeed"
              }
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        },
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE",
          "FAN_DIRECTION",
          "FAN_LIGHT",
          "FAN_HOME_SHIELD"
        ]
      }
    }
  },
  "FAN-FDR0L0_FAR0L0": {
    "timestamp": 1683618305000,
    "size": 9547,
    "lastModified": 1683618305000,
    "name": "FDR0L0_FAR0L0_trigger.json",
    "informationModel": {
      "scheduleLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ]
      },
      "familyMembers": [
        ".*-FDR0L0$",
        ".*-FAR0L0$"
      ],
      "integration": {
        "smartthings": {
          "deviceProfileId": "905d20a8-5c5a-467a-99f7-bf31f3c22127"
        },
        "traits": [
          {
            "append_name": " Fan",
            "id": "FAN",
            "type": "switch",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H02",
                "min": 1,
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "on": 1,
                  "off": 0
                }
              }
            },
            "appliedDomain": [
              "alexa",
              "ifttt"
            ],
            "description": "Fanimation fanSync-FDR0L0/FAR0L0 FAN"
          },
          {
            "appliedDomain": [
              "googlehome"
            ],
            "id": "GHFAN",
            "attributes": {
              "fan_speed": {
                "key": "H02",
                "reversible": {
                  "key": "H06",
                  "values": {
                    "normal": 2,
                    "reverse": 2
                  }
                },
                "values": [
                  {
                    "speed_name": "low",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "low",
                          "speed 1"
                        ]
                      }
                    ],
                    "value": 33
                  },
                  {
                    "speed_name": "medium",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "medium",
                          "speed 2"
                        ]
                      }
                    ],
                    "value": 66
                  },
                  {
                    "speed_name": "high",
                    "speed_values": [
                      {
                        "lang": "en",
                        "speed_synonym": [
                          "high",
                          "speed 3"
                        ]
                      }
                    ],
                    "value": 100
                  }
                ],
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR0L0/FAR0L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STFAN",
            "attributes": {
              "fan_speed": {
                "max": 100,
                "deTransform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "before": [
                  {
                    "key": "H00",
                    "value": 1
                  }
                ],
                "transform": {
                  "0": 0,
                  "1": 33,
                  "2": 66,
                  "3": 100
                },
                "min": 1,
                "key": "H02"
              },
              "on_off": {
                "key": "H00",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "fan",
            "append_name": " Fan",
            "description": "Fanimation fanSync-FDR0L0/FAR0L0 FAN"
          },
          {
            "appliedDomain": [
              "smartthings"
            ],
            "id": "STLIGHT",
            "attributes": {
              "percentage": {
                "max": 100,
                "key": "H0C",
                "min": 1,
                "before": [
                  {
                    "key": "H0B",
                    "value": 1
                  }
                ]
              },
              "on_off": {
                "key": "H0B",
                "values": {
                  "off": 0,
                  "on": 1
                }
              }
            },
            "type": "light",
            "append_name": " Light",
            "description": "Fanimation fanSync-FDR0L0/FAR0L0 LIGHT"
          }
        ]
      },
      "images": {
        "thumbnail": {
          "uri": "https://fanimation.apps.exosite.io/file_manager/FAN-FDR0L0_FAR0L0-thumbnail-1545043564"
        }
      },
      "eventCollections": [
        {
          "type": "triggerEvent",
          "name": "fan_switched_on",
          "conditions": [
            {
              "op": "eq",
              "target": 1,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_switched_off",
          "conditions": [
            {
              "op": "eq",
              "target": 0,
              "key": "H00"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_minimum",
          "conditions": [
            {
              "op": "lte",
              "target": 25,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_50",
          "conditions": [
            {
              "op": "eq",
              "target": 50,
              "key": "H02"
            }
          ]
        },
        {
          "type": "triggerEvent",
          "name": "fan_speed_at_maximum",
          "conditions": [
            {
              "op": "eq",
              "target": 100,
              "key": "H02"
            }
          ]
        }
      ],
      "deviceId": "F",
      "errorFields": [
        {
          "key": "H0E",
          "values": [
            {
              "value": 250,
              "text": "Parameter error"
            },
            {
              "value": 251,
              "text": "Parameter length error"
            },
            {
              "value": 252,
              "text": "Memory allocate failed"
            },
            {
              "value": 253,
              "text": "Send error"
            },
            {
              "value": 254,
              "text": "Unknown commands"
            },
            {
              "value": 255,
              "text": "Unknown fields"
            },
            {
              "value": 256,
              "text": "Too many entries"
            },
            {
              "value": 257,
              "text": "Under voltage"
            },
            {
              "value": 258,
              "text": "Over voltage"
            },
            {
              "value": 259,
              "text": "Over current"
            },
            {
              "value": 260,
              "text": "Under speed"
            },
            {
              "value": 261,
              "text": "Over speed"
            },
            {
              "value": 262,
              "text": "Stalled fault"
            },
            {
              "value": 263,
              "text": "Open phase fault"
            },
            {
              "value": 264,
              "text": "Chase max speed"
            },
            {
              "value": 265,
              "text": "Over temperature"
            },
            {
              "value": 266,
              "text": "EEPROM error"
            },
            {
              "value": 267,
              "text": "Remote control did not learn"
            },
            {
              "value": 268,
              "text": "Driver IC not response"
            },
            {
              "value": 269,
              "text": "ACZ abnormal"
            }
          ]
        }
      ],
      "familyName": "FAN-FDR0L0_FAR0L0",
      "components": {
        "FAN_POWER": {
          "type": "large-toggle",
          "models": [
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.POWER"
        },
        "FAN_MODE": {
          "type": "button-group",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                }
              ],
              "key": "H01",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.NORMAL"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.NATURAL"
                }
              ]
            }
          ],
          "title": "INFORMATION_MODEL.FAN_MODE"
        },
        "FAN_POWER_AND_SPEED": {
          "type": "large-toggle-with-range",
          "models": [
            {
              "disable": [
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 0,
                      "key": "H00"
                    }
                  ]
                },
                {
                  "conditions": [
                    {
                      "op": "eq",
                      "target": 1,
                      "key": "H01"
                    }
                  ]
                }
              ],
              "key": "H02",
              "values": [
                {
                  "text": "INFORMATION_MODEL.LOW",
                  "value": 33
                },
                {
                  "text": "INFORMATION_MODEL.MIDDLE",
                  "value": 66
                },
                {
                  "text": "INFORMATION_MODEL.HIGH",
                  "value": 100
                }
              ]
            },
            {
              "key": "H00",
              "values": [
                {
                  "value": 0,
                  "text": "INFORMATION_MODEL.OFF"
                },
                {
                  "value": 1,
                  "text": "INFORMATION_MODEL.ON"
                }
              ]
            }
          ],
          "title": ""
        }
      },
      "controlLayout": {
        "primary": [
          "FAN_POWER_AND_SPEED"
        ],
        "secondary": [
          "FAN_MODE"
        ]
      }
    }
  }
}
```