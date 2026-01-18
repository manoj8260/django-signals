# Django Signals Demo

A Django project demonstrating real-world usage of **Django signals**
including pre-save, post-save, pre-delete, and many-to-many change tracking.

---

## Implemented Signals

- `pre_save` → Automatic slug generation
- `post_save` → User welcome notification
- `pre_delete` → Backup before deletion
- `m2m_changed` → Track tag add/remove actions

---

## Signal Examples

### Automatic Slug Generation
- Triggered before saving a Post
- Generates slug using `slugify(title)`

### User Welcome Notification
- Triggered on User creation
- Sends a welcome message (dummy email)

### Pre-Deletion Backup
- Copies Post data into `DeletedPost`
- Runs before actual deletion

### Many-to-Many Tracking
- Tracks tag additions and removals
- Logs affected tag IDs with timestamps

---

## Run Demo

```bash
python manage.py signals_demo
