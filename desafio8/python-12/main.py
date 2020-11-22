
doc = '''
#%RAML 1.0
baseUri: https://anypoint.mulesoft.com/mocking/api/v1/links/85fd2c71-8b3b-4ada-b3d1-3c22dff54587/ # 
title: Codenation API
version: v1
mediaType: application/json
protocols: [HTTP, HTTPS]

# Autenticacao usando token
securitySchemes:
    JWT:
        description: Autenticação com Token JWT.
        type: x-jwt
        describedBy:
            headers:
                Authorization:
                    description: Enviar o JSON Web Token no request.
                    type: string
                    required: true
            responses:
                401:
                  description: |
                    {"error": "permission denied"}
        settings:
            signatures : ['HMAC-SHA256']

#Estruturas da agentes
types:
  Agent:
    type: object
    discriminator: agent_id
    properties:
      agent_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 50
      status:
        type: boolean
      environment:
        type: string
        maxLength: 20
      version:
        type: string
        maxLength: 5
      address:
        type: string
        maxLength: 39
      user_id:
        type: integer
    example:
      agent_id: 1
      name: Joey
      status: true
      environment: Python
      version: ex
      address: 1.1.1.1
      user_id: 1
  Auth:
    type: object
    discriminator: token
    properties:
      token: 
        required: true
        type: string
  Event:
    type: object
    discriminator: event_id
    properties:
      event_id:
        required: true
        type: integer
      level:
        type: string
        maxLength: 20
      payload:
        type: string
      shelved:
        type: boolean
      data:
        type: datetime
      agent_id:
        type: integer
  Group:
    type: object
    discriminator: group_id
    properties:
      group_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 20
    example:
      name: example
      group_id: 666
  User:
    type: object
    discriminator: user_id
    properties:
      user_id:
        required: true
        type: integer
      name:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      password:
        type: string
        maxLength: 50
      last_login:
        type: string
      group_id:
        type: integer

#Funções da API
#  ------ Autenticador ------
/auth/token:
  post:
    description: Obtem token
    body:
      application/json:
        properties:
          name: string
          password: string
    responses:
      201:
        body:
          application/json: Auth[]
      400:
        body:
          application/json: |
            {"error": "Bad Request."}
#  ------ Agent ------
/agents:
  get:
    securedBy: JWT
    description: "Lista os agentes"
    responses:
      200:
        body:
          type: Agent[]
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
  post:
    securedBy: JWT
    description: "Atualiza um agente"
    body: #Parâmetro de entrada um cliente
      type: Agent
    responses:
      200:
        body:
          application/json: | 
            {"mensager": "Elemento adicionado com sucesso"}
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
      404:
        body:
          application/json: | 
            {"error": "Elemento não encontrado"}
  /{id}:
    get:
      securedBy: JWT
      responses:
        200:
          body:
            type: Agent
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    put:
      securedBy: JWT
      body:
        type: Agent
      responses:
        200:
          body:
            application/json: | 
              {"ok": "Elemento atualizado com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    delete:
      securedBy: JWT
      body:
        type: Agent
      responses:
        200:
          body:
            application/json: | 
              {"mensager": "Elemento removido com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
  /{id}/events:
      get:      
          description: Lista evento de agente
          securedBy: JWT
          responses:         
              200:               
                  body:
                      application/json: Event[]
              401:
                  body:
                      application/json: |
                          {"error": "Authorization Required"}
              404:
                  body:
                      application/json: |
                          {"error": "Not Found"}
      post:     
          description: Inclui um Evento dentro do ID AGent
          securedBy: JWT
          body:
              application/json: Event[]
          responses:
              201:
                  body:
                      application/json: |
                          {"message": "Created"}
              401:
                  body:
                      application/json: |
                          {"error": "Authorization Required"}
              404:
                  body:
                      application/json: |
                          {"error": "Not Found"}
      put:    
          description: Altera um Evento de um Agent
          securedBy: JWT
          body:
              application/json: Event[]
          responses:
              200:               
                  body:
                      application/json: Event[]
              401:
                body:
                  application/json: | 
                    {"error": "Acesso não autorizado"}
              404:
                body:
                  application/json: | 
                    {"error": "Elemento não encontrado"}
      delete: 
          description: Exclui um Evento de um Agent
          securedBy: JWT
          body:
              application/json: Event[]
          responses:
              200:               
                  body:
                      application/json: Event[] 
              401:
                body:
                  application/json: | 
                    {"error": "Acesso não autorizado"}
              404:
                body:
                  application/json: | 
                    {"error": "Elemento não encontrado"}
      /{id}:
          get:      
              description: Lista evento de ID
              securedBy: JWT
              responses:         
                  200:               
                      body:
                          application/json: Event[]
                  401:
                    body:
                      application/json: | 
                        {"error": "Acesso não autorizado"}
                  404:
                    body:
                      application/json: | 
                        {"error": "Elemento não encontrado"}
          post:     
              description: Cria um Evento dentro do ID 
              securedBy: JWT
              body:
                  application/json: Event[]
              responses:
                  201:
                      body:
                        application/json: |
                            {"message": "Elemento criado"}
                  401:
                    body:
                      application/json: | 
                        {"error": "Acesso não autorizado"}
                  404:
                    body:
                      application/json: | 
                        {"error": "Elemento não encontrado"}
          put:    
              description: Altera um Evento de um Agent
              securedBy: JWT
              body:
                  application/json: Event[]
              responses:
                  200:               
                      body:
                          application/json: Event[]
                  401:
                      body:
                          application/json: |
                              {"error": "Authorization Required"}
                  404:
                      body:
                          application/json: |
                              {"error": "Not Found"}
          delete:
              description: Exclui um Evento de um Agent
              securedBy: JWT
              body:
                  application/json: Event[]
              responses:
                  200:               
                      body:
                          application/json: Event[] 
                  401:
                      body:
                          application/json: |
                              {"error": "Authorization Required"}
                  404:
                      body:
                          application/json: |
                              {"error": "Not Found"}
    
#  ------ Group ------
/groups:
  get:
    securedBy: JWT
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
  post:
    securedBy: JWT
    body:
      type: Group
    responses:
      200:
        body:
          application/json: | 
            {"mensager": "Elemento adicionado com sucesso"}
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
      404:
        body:
          application/json: | 
            {"error": "Elemento não encontrado"}
  /{id}:
    get:
      securedBy: JWT
      responses:
        200:
          body:
            type: Group
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    put:
      securedBy: JWT
      body:
        type: Group
      responses:
        200:
          body:
            application/json: | 
              {"ok": "Elemento atualizado com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    delete:
      securedBy: JWT
      body:
        type: Group
      responses:
        200:
          body:
            application/json: | 
              {"mensager": "Elemento removido com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}

# ------ User ------
/users:
  get:
    securedBy: JWT
    responses:
      200:
        body:
          type: User[]
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
  post:
    securedBy: JWT
    body:
      type: User
    responses:
      200:
        body:
          application/json: | 
            {"mensager": "Elemento adicionado com sucesso"}
      401:
        body:
          application/json: | 
            {"error": "Acesso não autorizado"}
      404:
        body:
          application/json: | 
            {"error": "Elemento não encontrado"}
  /{id}:
    get:
      securedBy: JWT
      responses:
        200:
          body:
            type: User
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    put:
      securedBy: JWT
      body:
        type: User
      responses:
        200:
          body:
            application/json: | 
              {"ok": "Elemento atualizado com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
    delete:
      securedBy: JWT
      body:
        type: User
      responses:
        200:
          body:
            application/json: | 
              {"mensager": "Elemento removido com sucesso"}
        401:
          body:
            application/json: | 
              {"error": "Acesso não autorizado"}
        404:
          body:
            application/json: | 
              {"error": "Elemento não encontrado"}
# End Document



'''
