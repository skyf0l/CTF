//int check_flag(char * flag)
//{
//  size_t size;
//  int res;

//  size = strlen(flag);
//  if (size == 0x1d) {
    if (flag[0x13] == '6') {
      flag[6] = flag[6] + '\x03';
      if (flag[0x10] == 'n') {
        flag[0x14] = flag[0x14] + -8;
        flag[0x1a] = flag[0x1a] + -6;
        if (flag[0xd] == 'r') {
          if (flag[0x14] == '%') {
            if (flag[0xf] == 'n') {
              if (flag[10] == 'p') {
                flag[0x10] = flag[0x10] + '\a';
                if (flag[0x10] == 'u') {
                  if (flag[3] == '{') {
                    flag[9] = flag[9] + '\x01';
                    if (flag[0x13] == '6') {
                      if (flag[0x15] == 'q') {
                        if (flag[0x15] == 'q') {
                          if (flag[2] == 'n') {
                            flag[0xc] = flag[0xc] + -1;
                            if (flag[0] == 's') {
                              if (flag[0] == 's') {
                                if (flag[7] == 'l') {
                                  if (flag[0xe] == 'u') {
                                    flag[0x11] = flag[0x11] + '\x06';
                                    flag[5] = flag[5] + '\x05';
                                    if (flag[0xc] == ',') {
                                      flag[0x16] = flag[0x16] + '\x05';
                                      flag[0x11] = flag[0x11] + -8;
                                      flag[3] = flag[3] + '\x05';
                                      flag[0x10] = flag[0x10] + -4;
                                      if (flag[0xf] == 'n') {
                                        if (flag[0xe] == 'u') {
                                          flag[7] = flag[7] + -9;
                                          if (flag[4] == 'b') {
                                            if (flag[0xe] == 'u') {
                                              flag[0x18] = flag[0x18] + -10;
                                              flag[0] = flag[0] + -3;
                                              if (flag[6] == 'o') {
                                                flag[0xb] = flag[0xb] + '\a';
                                                flag[1] = flag[1] + -2;
                                                flag[0x19] = flag[0x19] + '\x05';
                                                if (flag[0x12] == 'n') {
                                                  if (flag[7] == 'c') {
                                                    flag[0x18] = flag[0x18] + -8;
                                                    flag[0x12] = flag[0x12] + -9;
                                                    flag[0x14] = flag[0x14] + -4;
                                                    if (flag[0x16] == 'z') {
                                                      flag[6] = flag[6] + -9;
                                                      flag[10] = flag[10] + '\a';
                                                      flag[0x14] = flag[0x14] + '\x04';
                                                      if (flag[0xf] == 'n') {
                                                        flag[0x18] = flag[0x18] + '\b';
                                                        flag[0x13] = flag[0x13] + -2;
                                                        flag[0x19] = flag[0x19] + '\a';
                                                        if (flag[2] == 'n') {
                                                          if (flag[0x17] == '1') {
                                                            flag[0] = flag[0] + -8;
                                                            if (flag[0x14] == '%') {
                                                              if (flag[1] == 's') {
                                                                if (flag[6] == 'f') {
                                                                  flag[0x14] = flag[0x14] + '\x04';
                                                                  if (flag[2] == 'n') {
                                                                    if (flag[0x18] == 'Y') {
                                                                      flag[0x17] = flag[0x17] + -5;
                                                                      if (flag[0x1c] == '}') {
                                                                        flag[9] = flag[9] + '\x02';
                                                                        flag[0x16] = flag[0x16] + -6;
                                                                        flag[8] = flag[8] + '\x03';
                                                                        if (flag[10] == 'w') {
                                                                          flag[0x11] = flag[0x11] + '\t';
                                                                          if (flag[0x10] == 'q') {
                                                                            if (flag[0] == 'h') {
                                                                              if (flag[4] == 'b') {
                                                                                flag[0xc] = flag[0xc] + -2;
                                                                                flag[0xd] = flag[0xd] + -4;
                                                                                flag[0x10] = flag[0x10] + -4;
                                                                                if (flag[2] == 'n') {
                                                                                  flag[9] = flag[9] + -7;
                                                                                  flag[7] = flag[7] + '\b';
                                                                                  flag[8] = flag[8] + '\x04';
                                                                                  flag[0xd] = flag[0xd] + -10;
                                                                                  flag[0x1a] = flag[0x1a] + '\a';
                                                                                  if (flag[0xe] == 'u') {
                                                                                    if (flag[0x16] == 't') {
                                                                                      if (flag[2] == 'n') {
                                                                                        flag[0xf] = flag[0xf] + -3;
                                                                                        if (flag[0x1a] == 'm') {
                                                                                          flag[6] = flag[6] + '\x05';
                                                                                          flag[0x13] = flag[0x13] + -10;
                                                                                          flag[0x1c] = flag[0x1c] + '\x04';
                                                                                          if (flag[6] == 'k') {
                                                                                            flag[3] = flag[3] + -9;
                                                                                            if (flag[6] == 'k') {
                                                                                              flag[0x11] = flag[0x11] + -5;
                                                                                              flag[0x11] = flag[0x11] + -6;
                                                                                              if (flag[1] == 's') {
                                                                                                if (flag[0x12] == 'e') {
                                                                                                  flag[4] = flag[4] + '\x05';
                                                                                                  if (flag[6] == 'k') {
                                                                                                    if (flag[0xc] == '*') {
                                                                                                      if (flag[2] == 'n') {
                                                                                                        if (flag[0x18] == 'Y') {
                                                                                                          flag[6] = flag[6] + -7;
                                                                                                          if (flag[0x17] == ',') {
                                                                                                            if (flag[0x15] == 'q') {
                                                                                                              flag[0x1c] = flag[0x1c] + -8;
                                                                                                              flag[0] = flag[0] + '\x03';
                                                                                                              flag[3] = flag[3] + -9;
                                                                                                              flag[0xf] = flag[0xf] + '\x03';
                                                                                                              flag[8] = flag[8] + -9;
                                                                                                              if (flag[2] == 'n') {
                                                                                                                if (flag[0x1b] == 'y') {
                                                                                                                  if (flag[0x1c] == 'y') {
                                                                                                                    if (flag[0x13] == '*') {
                                                                                                                      if (flag[8] == 'f') {
                                                                                                                        if (flag[0x1c] == 'y') {
                                                                                                                          if (flag[9] == ',') {
                                                                                                                            if (flag[2] == 'n') {
                                                                                                                              if (flag[0xd] == 'd') {
                                                                                                                                if (flag[0x16] == 't') {
                                                                                                                                  if (flag[5] == '8') {
                                                                                                                                    if (flag[7] == 'k') {
                                                                                                                                      if (flag[9] == ',') {
                                                                                                                                        if (flag[1] == 's') {
                                                                                                                                          if (flag[0] == 'k') {
                                                                                                                                            if (flag[8] == 'f') {
                                                                                                                                              if (flag[1] == 's') {
                                                                                                                                                if (flag[0x15] == 'q') {
                                                                                                                                                  if (flag[0x1b] == 'y') {
                                                                                                                                                    if (flag[0x13] == '*') {
                                                                                                                                                      if (flag[3] == 'n') {
                                                                                                                                                        if (flag[0x14] == ')') {
                                                                                                                                                          if (flag[0xc] == '*') {
                                                                                                                                                            if (flag[0x17] == ',') {
                                                                                                                                                              if (flag[3] == 'n') {
                                                                                                                                                                if (flag[0x16] == 't') {
                                                                                                                                                                  if (flag[0x1c] == 'y') {
                                                                                                                                                                    if (flag[6] == 'd') {
                                                                                                                                                                      if (flag[2] == 'n') {
                                                                                                                                                                        if (flag[0] == 'k') {
                                                                                                                                                                          if (flag[0] == 'k') {
                                                                                                                                                                            if (flag[8] == 'f') {
                                                                                                                                                                              if (flag[0x13] == '*') {
                                                                                                                                                                                if (flag[0xe] == 'u') {
                                                                                                                                                                                  if (flag[7] == 'k') {
                                                                                                                                                                                    if (flag[0x18] == 'Y') {
                                                                                                                                                                                      if (flag[0x19] == 'w') {
                                                                                                                                                                                        if (flag[0x11] == '-') {
                                                                                                                                                                                          if (flag[4] == 'g') {
                                                                                                                                                                                            if (flag[0x17] == ',') {
                                                                                                                                                                                              if (flag[5] == '8') {
                                                                                                                                                                                                if (flag[0xc] == '*') {
                                                                                                                                                                                                  if (flag[0x1b] == 'y') {
                                                                                                                                                                                                    if (flag[0xe] == 'u') {
                                                                                                                                                                                                      if (flag[8] == 'f') {
                                                                                                                                                                                                        if (flag[0xc] == '*') {
                                                                                                                                                                                                          if (flag[4] == 'g') {
                                                                                                                                                                                                            if (flag[0x1c] == 'y') {
                                                                                                                                                                                                              if (flag[8] == 'f') {
                                                                                                                                                                                                                if (flag[0x1c] == 'y') {
                                                                                                                                                                                                                  if (flag[0xc] == '*') {
                                                                                                                                                                                                                    if (flag[3] == 'n') {
                                                                                                                                                                                                                      if (flag[8] == 'f') {
                                                                                                                                                                                                                        if (flag[0x19] == 'w') {
                                                                                                                                                                                                                          if (flag[3] == 'n') {
                                                                                                                                                                                                                            if (flag[6] == 'd') {
                                                                                                                                                                                                                              if (flag[7] == 'k') {
                                                                                                                                                                                                                                if (flag[0x19] == 'w') {
                                                                                                                                                                                                                                  if (flag[0xb] == '<') {
                                                                                                                                                                                                                                    if (flag[0x1b] == 'y') {
                                                                                                                                                                                                                                      if (flag[0xd] == 'd') {
                                                                                                                                                                                                                                        if (flag[0x1b] == 'y') {
                                                                                                                                                                                                                                          res = 1;
                                                                                                                                                                                                                                        } else {
                                                                                                                                                                                                                                          res = 0;
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                      } else {
                                                                                                                                                                                                                                        res = 0;
                                                                                                                                                                                                                                      }
                                                                                                                                                                                                                                    } else {
                                                                                                                                                                                                                                      res = 0;
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                  } else {
                                                                                                                                                                                                                                    res = 0;
                                                                                                                                                                                                                                  }
                                                                                                                                                                                                                                } else {
                                                                                                                                                                                                                                  res = 0;
                                                                                                                                                                                                                                }
                                                                                                                                                                                                                              } else {
                                                                                                                                                                                                                                res = 0;
                                                                                                                                                                                                                              }
                                                                                                                                                                                                                            } else {
                                                                                                                                                                                                                              res = 0;
                                                                                                                                                                                                                            }
                                                                                                                                                                                                                          } else {
                                                                                                                                                                                                                            res = 0;
                                                                                                                                                                                                                          }
                                                                                                                                                                                                                        } else {
                                                                                                                                                                                                                          res = 0;
                                                                                                                                                                                                                        }
                                                                                                                                                                                                                      } else {
                                                                                                                                                                                                                        res = 0;
                                                                                                                                                                                                                      }
                                                                                                                                                                                                                    } else {
                                                                                                                                                                                                                      res = 0;
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                  } else {
                                                                                                                                                                                                                    res = 0;
                                                                                                                                                                                                                  }
                                                                                                                                                                                                                } else {
                                                                                                                                                                                                                  res = 0;
                                                                                                                                                                                                                }
                                                                                                                                                                                                              } else {
                                                                                                                                                                                                                res = 0;
                                                                                                                                                                                                              }
                                                                                                                                                                                                            } else {
                                                                                                                                                                                                              res = 0;
                                                                                                                                                                                                            }
                                                                                                                                                                                                          } else {
                                                                                                                                                                                                            res = 0;
                                                                                                                                                                                                          }
                                                                                                                                                                                                        } else {
                                                                                                                                                                                                          res = 0;
                                                                                                                                                                                                        }
                                                                                                                                                                                                      } else {
                                                                                                                                                                                                        res = 0;
                                                                                                                                                                                                      }
                                                                                                                                                                                                    } else {
                                                                                                                                                                                                      res = 0;
                                                                                                                                                                                                    }
                                                                                                                                                                                                  } else {
                                                                                                                                                                                                    res = 0;
                                                                                                                                                                                                  }
                                                                                                                                                                                                } else {
                                                                                                                                                                                                  res = 0;
                                                                                                                                                                                                }
                                                                                                                                                                                              } else {
                                                                                                                                                                                                res = 0;
                                                                                                                                                                                              }
                                                                                                                                                                                            } else {
                                                                                                                                                                                              res = 0;
                                                                                                                                                                                            }
                                                                                                                                                                                          } else {
                                                                                                                                                                                            res = 0;
                                                                                                                                                                                          }
                                                                                                                                                                                        } else {
                                                                                                                                                                                          res = 0;
                                                                                                                                                                                        }
                                                                                                                                                                                      } else {
                                                                                                                                                                                        res = 0;
                                                                                                                                                                                      }
                                                                                                                                                                                    } else {
                                                                                                                                                                                      res = 0;
                                                                                                                                                                                    }
                                                                                                                                                                                  } else {
                                                                                                                                                                                    res = 0;
                                                                                                                                                                                  }
                                                                                                                                                                                } else {
                                                                                                                                                                                  res = 0;
                                                                                                                                                                                }
                                                                                                                                                                              } else {
                                                                                                                                                                                res = 0;
                                                                                                                                                                              }
                                                                                                                                                                            } else {
                                                                                                                                                                              res = 0;
                                                                                                                                                                            }
                                                                                                                                                                          } else {
                                                                                                                                                                            res = 0;
                                                                                                                                                                          }
                                                                                                                                                                        } else {
                                                                                                                                                                          res = 0;
                                                                                                                                                                        }
                                                                                                                                                                      } else {
                                                                                                                                                                        res = 0;
                                                                                                                                                                      }
                                                                                                                                                                    } else {
                                                                                                                                                                      res = 0;
                                                                                                                                                                    }
                                                                                                                                                                  } else {
                                                                                                                                                                    res = 0;
                                                                                                                                                                  }
                                                                                                                                                                } else {
                                                                                                                                                                  res = 0;
                                                                                                                                                                }
                                                                                                                                                              } else {
                                                                                                                                                                res = 0;
                                                                                                                                                              }
                                                                                                                                                            } else {
                                                                                                                                                              res = 0;
                                                                                                                                                            }
                                                                                                                                                          } else {
                                                                                                                                                            res = 0;
                                                                                                                                                          }
                                                                                                                                                        } else {
                                                                                                                                                          res = 0;
                                                                                                                                                        }
                                                                                                                                                      } else {
                                                                                                                                                        res = 0;
                                                                                                                                                      }
                                                                                                                                                    } else {
                                                                                                                                                      res = 0;
                                                                                                                                                    }
                                                                                                                                                  } else {
                                                                                                                                                    res = 0;
                                                                                                                                                  }
                                                                                                                                                } else {
                                                                                                                                                  res = 0;
                                                                                                                                                }
                                                                                                                                              } else {
                                                                                                                                                res = 0;
                                                                                                                                              }
                                                                                                                                            } else {
                                                                                                                                              res = 0;
                                                                                                                                            }
                                                                                                                                          } else {
                                                                                                                                            res = 0;
                                                                                                                                          }
                                                                                                                                        } else {
                                                                                                                                          res = 0;
                                                                                                                                        }
                                                                                                                                      } else {
                                                                                                                                        res = 0;
                                                                                                                                      }
                                                                                                                                    } else {
                                                                                                                                      res = 0;
                                                                                                                                    }
                                                                                                                                  } else {
                                                                                                                                    res = 0;
                                                                                                                                  }
                                                                                                                                } else {
                                                                                                                                  res = 0;
                                                                                                                                }
                                                                                                                              } else {
                                                                                                                                res = 0;
                                                                                                                              }
                                                                                                                            } else {
                                                                                                                              res = 0;
                                                                                                                            }
                                                                                                                          } else {
                                                                                                                            res = 0;
                                                                                                                          }
                                                                                                                        } else {
                                                                                                                          res = 0;
                                                                                                                        }
                                                                                                                      } else {
                                                                                                                        res = 0;
                                                                                                                      }
                                                                                                                    } else {
                                                                                                                      res = 0;
                                                                                                                    }
                                                                                                                  } else {
                                                                                                                    res = 0;
                                                                                                                  }
                                                                                                                } else {
                                                                                                                  res = 0;
                                                                                                                }
                                                                                                              } else {
                                                                                                                res = 0;
                                                                                                              }
                                                                                                            } else {
                                                                                                              res = 0;
                                                                                                            }
                                                                                                          } else {
                                                                                                            res = 0;
                                                                                                          }
                                                                                                        } else {
                                                                                                          res = 0;
                                                                                                        }
                                                                                                      } else {
                                                                                                        res = 0;
                                                                                                      }
                                                                                                    } else {
                                                                                                      res = 0;
                                                                                                    }
                                                                                                  } else {
                                                                                                    res = 0;
                                                                                                  }
                                                                                                } else {
                                                                                                  res = 0;
                                                                                                }
                                                                                              } else {
                                                                                                res = 0;
                                                                                              }
                                                                                            } else {
                                                                                              res = 0;
                                                                                            }
                                                                                          } else {
                                                                                            res = 0;
                                                                                          }
                                                                                        } else {
                                                                                          res = 0;
                                                                                        }
                                                                                      } else {
                                                                                        res = 0;
                                                                                      }
                                                                                    } else {
                                                                                      res = 0;
                                                                                    }
                                                                                  } else {
                                                                                    res = 0;
                                                                                  }
                                                                                } else {
                                                                                  res = 0;
                                                                                }
                                                                              } else {
                                                                                res = 0;
                                                                              }
                                                                            } else {
                                                                              res = 0;
                                                                            }
                                                                          } else {
                                                                            res = 0;
                                                                          }
                                                                        } else {
                                                                          res = 0;
                                                                        }
                                                                      } else {
                                                                        res = 0;
                                                                      }
                                                                    } else {
                                                                      res = 0;
                                                                    }
                                                                  } else {
                                                                    res = 0;
                                                                  }
                                                                } else {
                                                                  res = 0;
                                                                }
                                                              } else {
                                                                res = 0;
                                                              }
                                                            } else {
                                                              res = 0;
                                                            }
                                                          } else {
                                                            res = 0;
                                                          }
                                                        } else {
                                                          res = 0;
                                                        }
                                                      } else {
                                                        res = 0;
                                                      }
                                                    } else {
                                                      res = 0;
                                                    }
                                                  } else {
                                                    res = 0;
                                                  }
                                                } else {
                                                  res = 0;
                                                }
                                              } else {
                                                res = 0;
                                              }
                                            } else {
                                              res = 0;
                                            }
                                          } else {
                                            res = 0;
                                          }
                                        } else {
                                          res = 0;
                                        }
                                      } else {
                                        res = 0;
                                      }
                                    } else {
                                      res = 0;
                                    }
                                  } else {
                                    res = 0;
                                  }
                                } else {
                                  res = 0;
                                }
                              } else {
                                res = 0;
                              }
                            } else {
                              res = 0;
                            }
                          } else {
                            res = 0;
                          }
                        } else {
                          res = 0;
                        }
                      } else {
                        res = 0;
                      }
                    } else {
                      res = 0;
                    }
                  } else {
                    res = 0;
                  }
                } else {
                  res = 0;
                }
              } else {
                res = 0;
              }
            } else {
              res = 0;
            }
          } else {
            res = 0;
          }
        } else {
          res = 0;
        }
      } else {
        res = 0;
      }
    } else {
      res = 0;
    }
  } else {
    res = 0;
  }
  return res;
}
