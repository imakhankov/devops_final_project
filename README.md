# DevOps Final Project
                                                                                                                                                                                                          
  Полноценный стек развёрнутый автоматически через Ansible и Docker.                                                                                                                                      
   
  ## Стек                                                                                                                                                                                      
                                                                                                                                                                                                        
  - Frontend — статический сайт в Nginx-контейнере                                                                                                                                                        
  - Backend — Python Flask API
  - Database — PostgreSQL с persistent volume                                                                                                                                                             
  - Nginx — reverse proxy                                                                                                                                                                                 
   
  ## Быстрый старт                                                                                                                                                                                        
                                                                                                                                                                                                        
  Развернуть весь стек одной командой:                                                                                                                                                                    
   
      ansible-playbook -i ansible/inventory/hosts ansible/deploy.yml                                                                                                                                      
                                                                                                                                                                                                        
  ## Маршруты                                                                                                                                                                                             
                                                                                                                                                                                                        
  - / → Frontend                                                                                                                                                                                          
  - /api/health → Backend healthcheck
  - /api/hello → Backend hello                                                                                                                                                                            
                                                                                                                                                                                                        
  ## Структура проекта

      devops_final_project/                                                                                                                                                                               
      ├── ansible/
      │   ├── deploy.yml                                                                                                                                                                                  
      │   └── inventory/hosts                                                                                                                                                                           
      ├── backend/
      │   ├── app.py
      │   ├── requirements.txt
      │   └── Dockerfile                                                                                                                                                                                  
      ├── frontend/
      │   ├── index.html                                                                                                                                                                                  
      │   └── Dockerfile                                                                                                                                                                                
      ├── nginx/
      │   └── nginx.conf                                                                                                                                                                                  
      └── docker/
          ├── docker-compose.yml                                                                                                                                                                          
          └── .env.example                                                                                                                                                                              
                                                                                                                                                                                                          
  ## Требования
                                                                                                                                                                                                          
  - Ansible                                                                                                                                                                                             
  - Docker
  - SSH доступ к серверу
