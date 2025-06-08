## Part 2: SSH Brute Force Attack

### 1. Build and Start Docker Containers

```bash
cd ssh_brute_force/docker_simulation
docker-compose down  # Clean up any existing containers
docker system prune -f  # Remove unused containers/images
docker-compose up --build
```

Expected output:
```bash
Creating network "docker_simulation_default" with the default driver
Building target
Step 1/8 : FROM ubuntu:20.04
...
Successfully built abc123def456
Successfully tagged docker_simulation-target:latest
Creating ctf_target ... done
Attaching to ctf_target
ctf_target    | Server listening on 0.0.0.0 port 22.
```

### 2. Run the Attack (in a new terminal)

```bash
# In a new terminal
python brute_force_ssh.py
```

Expected output:
```bash
Loading password list...
Starting SSH brute force attack...
Trying password: apple... Failed
Trying password: banana... Failed
Trying password: mango... Success!
Password found: mango
Attack completed in 3.45 seconds
```

### 3. Verify Access

```bash
ssh target_user@localhost -p 2222
# Enter password: mango
```

Expected output:
```bash
The authenticity of host '[localhost]:2222' can't be established.
ECDSA key fingerprint is SHA256:abcdef123456...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
target_user@localhost's password: 
Welcome to Ubuntu 20.04 LTS
target_user@container:~$ 
```

## Cleanup

```bash
# Stop and remove containers
docker-compose down

# Deactivate virtual environment
deactivate
```

Expected output:
```bash
Stopping ctf_target ... done
Removing ctf_target ... done
Removing network docker_simulation_default
```

## Security Note

This is an educational demonstration. The techniques shown should only be used on systems you own or have explicit permission to test. Unauthorized access attempts are illegal.

## Technical Details

### Target Container
- Ubuntu 20.04
- OpenSSH Server
- Port 2222 -> 22
- Non-root user account

### Attacker Container
- Python 3.9
- Paramiko for SSH
- Rate-limited attempts
- Dictionary-based attack

### Substitution Cipher
- Monoalphabetic substitution
- Uppercase letters only
- No special characters

## Troubleshooting

### Common Issues

1. Port Conflict
```bash
# If port 2222 is already in use
docker-compose down
sudo lsof -i :2222  # Find conflicting process
sudo kill <PID>     # Stop conflicting process
```

2. Container Access Issues
```bash
# Check container status
docker ps
docker logs ctf_target
```

3. SSH Connection Problems
```bash
# Enable verbose SSH output
ssh -v target_user@localhost -p 2222
```

## License

MIT License - See LICENSE file for details 
