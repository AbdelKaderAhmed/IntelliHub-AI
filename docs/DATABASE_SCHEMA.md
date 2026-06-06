Database Schema

tenants

id

name

created_at

users

id

tenant_id

email

password_hash

role

created_at

documents

id

tenant_id

filename

storage_path

uploaded_by

uploaded_at

conversations

id

tenant_id

user_id

created_at

messages

id

conversation_id

role

content

created_at

audit_logs

id

tenant_id

user_id

action

created_at
