# 🤝 Contributing to fire

Welcome to `fire`! Even though this repository began as a personal milestone and first-ever repository in May 2018, it now serves as a model of clean Gitflow practices.

---

## 🌿 Gitflow Workflow

We follow standard Gitflow conventions across our 3 branches:

```
  master ───────────────●─────────────────────────● (Release/Monument)
                         \                       /
  develop ────────────────●────────●────────────●   (Active Development)
                           \      /
  feature/hello-github ─────●────●                  (Feature Development)
```

### Branch Roles

1. **`master`**: Protected production branch. Contains stable, tagged releases and the permanent commemorative monument.
2. **`develop`**: Primary staging and development branch. All feature branches merge here first.
3. **`feature/*`**: Feature-specific branches created off `develop`. Once tested, they are submitted as Pull Requests back into `develop`.

---

## 📝 Commit Message Conventions

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` A new feature or capability (e.g. `feat(cli): add flame animation`)
- `docs:` Documentation updates (e.g. `docs: polish README`)
- `fix:` Bug fixes
- `refactor:` Code improvements that don't change behavior
- `chore:` Maintenance, configs, changelog updates

---

## 🚀 Creating a Feature Branch

```bash
# 1. Update your local develop branch
git checkout develop
git pull origin develop

# 2. Create your new feature branch
git checkout -b feature/your-feature-name

# 3. Make changes and commit
git add .
git commit -m "feat(scope): your descriptive message"

# 4. Push to remote and open a Pull Request
git push origin feature/your-feature-name
```
