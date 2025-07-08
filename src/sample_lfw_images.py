import os
import random
import shutil

# Configuration
LFW_ROOT = "data/lfw/archive/lfw-deepfunneled/lfw-deepfunneled"
KNOWN_DIR = "data/known_faces"
BATCH_DIR = "data/batch_images"
NUM_PEOPLE = 5  # Number of people to sample as known faces
IMAGES_PER_PERSON_KNOWN = 1  # Images per person for known faces
IMAGES_PER_PERSON_BATCH = 2  # Images per person for batch processing

os.makedirs(KNOWN_DIR, exist_ok=True)
os.makedirs(BATCH_DIR, exist_ok=True)

people = [p for p in os.listdir(LFW_ROOT) if os.path.isdir(os.path.join(LFW_ROOT, p))]
selected_people = random.sample(people, NUM_PEOPLE)

print(f"Selected people: {selected_people}")

# Copy known images
for person in selected_people:
    person_dir = os.path.join(LFW_ROOT, person)
    images = [img for img in os.listdir(person_dir) if img.lower().endswith('.jpg')]
    chosen_known = random.sample(images, min(IMAGES_PER_PERSON_KNOWN, len(images)))
    for img in chosen_known:
        src = os.path.join(person_dir, img)
        dst = os.path.join(KNOWN_DIR, f"{person}_{img}")
        shutil.copy(src, dst)

# Copy batch images (can include known and unknown people)
for person in selected_people:
    person_dir = os.path.join(LFW_ROOT, person)
    images = [img for img in os.listdir(person_dir) if img.lower().endswith('.jpg')]
    chosen_batch = random.sample(images, min(IMAGES_PER_PERSON_BATCH, len(images)))
    for img in chosen_batch:
        src = os.path.join(person_dir, img)
        dst = os.path.join(BATCH_DIR, f"{person}_{img}")
        shutil.copy(src, dst)

# Optionally add some unknowns
other_people = [p for p in people if p not in selected_people]
unknown_people = random.sample(other_people, min(3, len(other_people)))
for person in unknown_people:
    person_dir = os.path.join(LFW_ROOT, person)
    images = [img for img in os.listdir(person_dir) if img.lower().endswith('.jpg')]
    if images:
        img = random.choice(images)
        src = os.path.join(person_dir, img)
        dst = os.path.join(BATCH_DIR, f"{person}_{img}")
        shutil.copy(src, dst)

print("Sample images copied for known and batch processing.")
