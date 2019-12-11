#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a
 * sorted singly linked list
 * @head: head address of linked list
 * @number: number property of the node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *past = NULL;

	if (!head)
		return (NULL);

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head)
		*head = new;
	else
	{
		for (; current->next && (current->n < new->n); current = current->next)
			past = current;

		if (!current->next)
			current->next = new;
		else if (!past)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			past->next = new;
			new->next = current;
		}
	}

	return (new);
}
