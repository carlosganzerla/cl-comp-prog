(defstruct (queue (:conc-name nil)) 
  buffer cache)

(defun enqueue (queue x)
  (push x (buffer queue)))

(defun %make-cache (queue)
  (dolist (e (buffer queue))
    (push (pop (buffer queue)) (cache queue))))

(defun peek (queue)
  (unless (cache queue)
    (%make-cache queue))
  (car (cache queue)))

(defun dequeue (queue)
  (unless (cache queue)
    (%make-cache queue))
  (pop (cache queue)))

(defun main ()
  (let ((queue (make-queue)))
    (dotimes (_ (read))
      (case (read)
        (1 (enqueue queue (read)))
        (2 (dequeue queue))
        (3 (format t "~A~%" (peek queue)))))))

(main)
