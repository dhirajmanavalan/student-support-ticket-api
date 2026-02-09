# Overall Flow

        Client (Browser / Requests Script)

                |

                v

        FastAPI Application

                |

                +-----------------------------+
                
                |                             |

        Auth Routes                  Ticket Routes

            (/login)                    (/tickets)

                |                             |

                v                             v

            JWT Handler                Business Logic

            (create / decode)          (role checks)

                |

                v

            In-Memory Storage
        
            (Users & Tickets)


# 🔐 Authentication Flow

        User (Student / Support)
                |
                v
            /login
                |
                v
        Verify credentials
                |
                v
        Generate JWT Token
                |
                v
        Token sent to client

# 🎓 Student Flow (Create & View Own Tickets)

        Student
        |
        | Authorization: Bearer <JWT>
        v
        POST /tickets
        |
        v
        Token verified
        |
        v
        Role = student
        |
        v
        Ticket created
        ---------------------------------------------------------------
        Student
        |
        | Authorization: Bearer <JWT>
        v
        GET /tickets
        |
        v
        Only student's tickets returned


# 🛠 Support Staff Flow (View All & Update Tickets)

        Support Staff
            |
            | Authorization: Bearer <JWT>
            v
        GET /tickets
            |
            v
        All student tickets returned
        ----------------------------------------------------------------
        Support Staff
            |
            | Authorization: Bearer <JWT>
            v
        PUT /tickets/{ticket_id}
            |
            v
        Ticket status updated