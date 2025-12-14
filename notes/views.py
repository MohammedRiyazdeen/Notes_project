from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note,Category
from django.contrib import messages 
from .forms import NoteForm,CategoryForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

@login_required
def Add_Note(request):
    if request.method == 'POST':
        n_form = NoteForm(request.POST or None, user=request.user)
        c_form = CategoryForm(request.POST, user=request.user)

        if n_form.is_valid():
            note = n_form.save(commit=False)
            note.user = request.user

            # If CategoryForm has data and is valid → create new category
            if c_form.is_valid() and c_form.cleaned_data.get('name'):
                cate = c_form.save(commit=False)
                cate.user = request.user
                cate.save()
                note.category = cate  # link new category to note

            # Otherwise → just use the dropdown selection from NoteForm
            note.save()
            messages.success(request, 'Your note has been created!')
            return redirect('list-note')
    else:
        n_form = NoteForm(user=request.user)
        c_form = CategoryForm(user=request.user)

    context = {
        "n_form": n_form,
        "c_form": c_form
    }
    return render(request, 'notes/add_note.html', context)


@login_required
def list_notes(request):
    search_query = request.GET.get('q')
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    if search_query:
        notes = notes.filter(
            Q( title__icontains = search_query  ) | Q(content__icontains = search_query)
            ).distinct()
        
   # Pagination
    paginator = Paginator(notes, 3)  # 3 notes per page
    page_number = request.GET.get('page')
    notes_page = paginator.get_page(page_number)

    return render(request, 'notes/list_notes.html', {
        "notes": notes_page,
        "query": search_query
    })



@login_required
def update_note(request, pk):
    obj = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == 'POST':
        n_form = NoteForm(request.POST, instance=obj, user=request.user)
        c_form = CategoryForm(request.POST, user=request.user)   # FIXED

        if n_form.is_valid():
            note = n_form.save(commit=False)
            note.user = request.user
            if c_form.is_valid() and c_form.cleaned_data.get('name'):
                cate = c_form.save(commit=False)
                cate.user = request.user
                cate.save()
                note.category = cate
            note.save()

            messages.success(request, 'Your note has been updated!')
            return redirect('list-note')
    else:
        n_form = NoteForm(instance=obj, user=request.user)
        c_form = CategoryForm(user=request.user)   # FIXED

    context = {
        "n_form": n_form,
        "c_form": c_form
    }
    return render(request, 'notes/update_notes.html', context)



@login_required    
def delete_note(request, pk):   
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, f'Your note has been deleted!')
        return redirect('list-note')
    
    return render(request, 'notes/delete_notes.html', {"note" :note})

# CRUD operation for category 
    

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, user=request.user)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            messages.success(request, f'Category has been created')
            return redirect('list-category')
    else:
        form = CategoryForm(user=request.user)

    return render(request, 'categories/add_category.html', {'form':form})



@login_required
def update_category(request, slug):
    obj = get_object_or_404(Category, slug=slug, user=request.user)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=obj, user=request.user)   
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your category has been updated!')
            return redirect('list-category')
    else:
        form = CategoryForm(instance=obj, user=request.user)   

    return render(request, 'categories/update_category.html', {"form": form})



@login_required
def list_category(request):
    categories = Category.objects.filter(user=request.user)

    return render(request, 'categories/list_category.html', {'categories':categories})



@login_required
def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug, user=request.user)
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'Your category has been Deleted!')
        return redirect('list-category')
         
    return render(request, 'categories/delete_category.html', {"category":category})



@login_required
def notes_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug, user=request.user)
    notes = Note.objects.filter(category=category, user=request.user)
    return render(request, 'categories/notes_by_category.html', {"category":category,"notes":notes})

